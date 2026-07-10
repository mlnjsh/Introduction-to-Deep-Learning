# RNN & LSTM Concepts — Keras (two datasets)

A concept-centric notebook series: **each notebook teaches one recurrent-network concept and
demonstrates it on BOTH datasets** — a text problem and a time-series problem — so you see how
the same idea plays out in the two settings RNN/LSTM are actually used for.

| Dataset | Task | RNN framing | Metric |
|---------|------|-------------|--------|
| **A) IMDB** movie reviews | binary sentiment | many-to-one **text classification** (Embedding → RNN → sigmoid) | accuracy |
| **B) Jena Climate** weather | temperature forecasting | sliding-window **sequence regression** | MAE (°C) |

Both are downloaded and cached by `01_sequence_data_prep` (run it first). Keras-only, CPU-sized.

## Notebooks

| # | Concept | IMDB side | Jena side |
|---|---------|-----------|-----------|
| 01 | **Sequence data prep** | tokenize → pad → embed; length histogram; decode a review | resample → standardize → sliding windows; window illustration |
| 02 | **SimpleRNN** | Embedding → SimpleRNN → sigmoid | SimpleRNN → Dense |
| 03 | **LSTM** (cell state + gates) | Embedding → LSTM | LSTM → Dense |
| 04 | **GRU** | Embedding → GRU | GRU → Dense |
| 05 | **Stacked / deep RNN** (`return_sequences`) | 2× LSTM | 2× LSTM |
| 06 | **Bidirectional** (+ forecasting caveat) | Embedding → BiLSTM | BiLSTM → Dense |
| 07 | **Dropout / recurrent_dropout / EarlyStopping** | reg vs no-reg, train-val gap | reg vs no-reg |
| 08 | **Comparison** SimpleRNN/LSTM/GRU/BiLSTM | table + curves | table + curves |
| 09 | **Save / load** | `.keras` + weights-only, verified | `.keras`, verified |
| 10 | **Text-specific** | Embedding internals, `mask_zero`, sequence-length sweep | — |
| 11 | **Time-series-specific** | — | univariate vs multivariate, 24-h multi-step, lookback sweep |

## Shared data module — `rnn_data.py`

All downloading/preprocessing lives here so the notebooks stay focused on concepts:

- `build_imdb_cache()` / `load_imdb()` → padded integer sequences (cached to `imdb_prepared.npz`).
- `build_jena_cache()` / `load_jena_series()` → standardized hourly weather (cached to `jena_prepared.npz`).
- `make_jena_datasets(lookback, horizon, feature_idx, multi_step, ...)` → windowed `tf.data`
  datasets for single-step or multi-step forecasting.
- SSL is patched via `truststore` at import, so the Keras downloads work on this Windows box.

## CPU sizing (this machine has no GPU)

Deliberately trimmed so the whole suite runs in reasonable time while still training real models:
IMDB subset 8k/4k, `maxlen=150`, vocab 10k; Jena first 20k hourly rows, `lookback=48`, few epochs.
Turn the knobs at the top of `rnn_data.py` up for a full-scale run.

## Kernel

Open with **`Python (DL course – TF 2.21)`** (TensorFlow 2.21). Run `01_sequence_data_prep`
first to build the caches, then any notebook top-to-bottom.
