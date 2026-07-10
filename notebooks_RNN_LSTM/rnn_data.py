"""
Shared data utilities for the RNN/LSTM notebook series (Keras only).

Two datasets:
  A) IMDB movie reviews  -> many-to-one text classification (built into Keras).
  B) Jena Climate weather -> sequence regression via sliding windows.

Design: heavy download + preprocessing happens ONCE and is cached to small .npz
files in this folder. Every notebook then calls the light `load_*` / `make_jena_*`
helpers, so the concept notebooks stay fast and focused.

CPU-friendly by default: subsets, short sequences, so the whole suite executes in
a reasonable time on this (GPU-less) machine.
"""
import os
import numpy as np

FOLDER = os.path.dirname(os.path.abspath(__file__))


def _ensure_ssl():
    """Patch Python's SSL to use the OS trust store — fixes CERTIFICATE_VERIFY_FAILED
    on this Windows box (corporate CA). Must run BEFORE any keras/urllib download."""
    try:
        import truststore
        truststore.inject_into_ssl()
    except Exception:
        # last-resort fallback: clear cert-bundle env vars that point at stale bundles
        for v in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
            os.environ.pop(v, None)


_ensure_ssl()   # patch at import so every downstream keras download is covered

# ---- CPU-friendly sizing knobs (used when building the caches) ----------------
IMDB_NUM_WORDS = 10000     # vocabulary size
IMDB_MAXLEN    = 150       # pad/truncate reviews to this many tokens
IMDB_N_TRAIN   = 8000      # subset of the 25k train reviews
IMDB_N_TEST    = 4000      # subset of the 25k test reviews

JENA_ROWS      = 20000     # keep the first N hourly rows (after resampling)
JENA_TRAIN_FRAC = 0.6      # fraction used for training statistics + train split
JENA_VAL_FRAC   = 0.2      # next fraction for validation


# ==============================================================================
# IMDB  (text -> binary sentiment)
# ==============================================================================
def build_imdb_cache(verbose=True):
    """Download IMDB, subset, pad, and cache to imdb_prepared.npz."""
    from tensorflow import keras
    _ensure_ssl()
    cache = os.path.join(FOLDER, "imdb_prepared.npz")
    (x_tr, y_tr), (x_te, y_te) = keras.datasets.imdb.load_data(num_words=IMDB_NUM_WORDS)

    # subset for CPU speed (data is already shuffled by Keras)
    x_tr, y_tr = x_tr[:IMDB_N_TRAIN], y_tr[:IMDB_N_TRAIN]
    x_te, y_te = x_te[:IMDB_N_TEST],  y_te[:IMDB_N_TEST]

    X_train = keras.utils.pad_sequences(x_tr, maxlen=IMDB_MAXLEN)
    X_test  = keras.utils.pad_sequences(x_te, maxlen=IMDB_MAXLEN)

    np.savez_compressed(cache,
                        X_train=X_train.astype("int32"), y_train=y_tr.astype("float32"),
                        X_test=X_test.astype("int32"),   y_test=y_te.astype("float32"),
                        num_words=IMDB_NUM_WORDS, maxlen=IMDB_MAXLEN)
    if verbose:
        print("IMDB cached:", X_train.shape, X_test.shape,
              "| vocab", IMDB_NUM_WORDS, "| maxlen", IMDB_MAXLEN)
    return cache


def load_imdb():
    """Return X_train, y_train, X_test, y_test (padded int sequences). Builds cache if missing."""
    cache = os.path.join(FOLDER, "imdb_prepared.npz")
    if not os.path.exists(cache):
        build_imdb_cache(verbose=False)
    d = np.load(cache)
    return d["X_train"], d["y_train"], d["X_test"], d["y_test"]


def imdb_config():
    return {"num_words": IMDB_NUM_WORDS, "maxlen": IMDB_MAXLEN}


# ==============================================================================
# JENA CLIMATE  (weather -> temperature forecasting)
# ==============================================================================
JENA_URL = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip"


def _download_jena_csv():
    """Return a path to the Jena CSV, downloading+unzipping robustly (TLS-safe)."""
    from tensorflow import keras
    _ensure_ssl()   # truststore fixes CERTIFICATE_VERIFY_FAILED on this Windows box (see memory)
    zip_path = keras.utils.get_file(
        "jena_climate_2009_2016.csv.zip", origin=JENA_URL, extract=True)
    # keras extracts next to the zip; locate the csv
    base = os.path.dirname(zip_path)
    for root, _, files in os.walk(base):
        for f in files:
            if f == "jena_climate_2009_2016.csv":
                return os.path.join(root, f)
    raise FileNotFoundError("Jena CSV not found after extraction")


def build_jena_cache(verbose=True):
    """Download Jena, resample hourly, subset, standardize (train stats), cache to jena_prepared.npz."""
    import pandas as pd
    cache = os.path.join(FOLDER, "jena_prepared.npz")
    csv = _download_jena_csv()
    df = pd.read_csv(csv)

    # 10-min data -> hourly (every 6th row), then keep the first JENA_ROWS rows
    df = df.iloc[5::6].reset_index(drop=True).iloc[:JENA_ROWS]
    feature_cols = [c for c in df.columns if c != "Date Time"]
    raw = df[feature_cols].values.astype("float32")
    target_idx = feature_cols.index("T (degC)")

    n_train = int(len(raw) * JENA_TRAIN_FRAC)
    mean = raw[:n_train].mean(axis=0)
    std  = raw[:n_train].std(axis=0)
    data = (raw - mean) / std                      # standardized features
    temp_norm = data[:, target_idx].copy()         # standardized target column

    np.savez_compressed(cache,
                        data=data, temp_norm=temp_norm,
                        temp_mean=np.float32(mean[target_idx]),
                        temp_std=np.float32(std[target_idx]),
                        target_idx=np.int32(target_idx),
                        n_train=np.int32(n_train),
                        feature_names=np.array(feature_cols))
    if verbose:
        print("Jena cached:", data.shape, "| features", len(feature_cols),
              "| target 'T (degC)' idx", target_idx, "| n_train", n_train)
    return cache


def load_jena_series():
    """Return dict with standardized `data` (N,F), `temp_norm` (N,), denorm stats, split, names."""
    cache = os.path.join(FOLDER, "jena_prepared.npz")
    if not os.path.exists(cache):
        build_jena_cache(verbose=False)
    d = np.load(cache, allow_pickle=True)
    return {
        "data": d["data"], "temp_norm": d["temp_norm"],
        "temp_mean": float(d["temp_mean"]), "temp_std": float(d["temp_std"]),
        "target_idx": int(d["target_idx"]), "n_train": int(d["n_train"]),
        "feature_names": list(d["feature_names"]),
    }


def make_jena_datasets(lookback=48, horizon=1, batch_size=128, feature_idx=None,
                       multi_step=None):
    """
    Build train/val tf.data datasets of sliding windows.

    lookback   : timesteps fed to the RNN (hours).
    horizon    : predict the temperature this many steps after the window ends (single-step).
    feature_idx: list of column indices to use as inputs (None = all features).
    multi_step : if set to an int H, predict the next H temperatures (many-to-many head);
                 overrides `horizon`.

    Returns (train_ds, val_ds, n_features).
    """
    from tensorflow import keras
    s = load_jena_series()
    data, temp = s["data"], s["temp_norm"]
    n_train = s["n_train"]
    n_val = int(len(data) * (JENA_TRAIN_FRAC + JENA_VAL_FRAC))

    inputs = data if feature_idx is None else data[:, feature_idx]
    n_features = inputs.shape[1]

    if multi_step:
        H = int(multi_step)
        # target for window starting at i = temp[i+lookback : i+lookback+H]
        seqs, tgts = [], []
        end = len(inputs) - lookback - H
        for i in range(end):
            seqs.append(inputs[i:i + lookback])
            tgts.append(temp[i + lookback:i + lookback + H])
        seqs = np.asarray(seqs, dtype="float32"); tgts = np.asarray(tgts, dtype="float32")
        tr = slice(0, n_train); va = slice(n_train, n_val)
        import tensorflow as tf
        train_ds = tf.data.Dataset.from_tensor_slices((seqs[tr], tgts[tr])).batch(batch_size)
        val_ds   = tf.data.Dataset.from_tensor_slices((seqs[va], tgts[va])).batch(batch_size)
        return train_ds, val_ds, n_features

    # single-step: target = temp `horizon` steps past the window end
    delay = lookback + (horizon - 1)
    train_ds = keras.utils.timeseries_dataset_from_array(
        inputs[:-delay], targets=temp[delay:], sequence_length=lookback,
        batch_size=batch_size, start_index=0, end_index=n_train, shuffle=False)
    val_ds = keras.utils.timeseries_dataset_from_array(
        inputs[:-delay], targets=temp[delay:], sequence_length=lookback,
        batch_size=batch_size, start_index=n_train, end_index=n_val, shuffle=False)
    return train_ds, val_ds, n_features


if __name__ == "__main__":
    build_imdb_cache()
    build_jena_cache()
    print("Both caches built.")
