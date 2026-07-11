# Introduction to Deep Learning

Interactive teaching tools **and** a hands-on notebook curriculum for an *Introduction to Deep
Learning* course, by **Dr. Milan Joshi** (MathCanvasMJ).

---

## 🧠 Neural Network Forward-Pass Visualizer

**▶ Open it live: https://mlnjsh.github.io/Introduction-to-Deep-Learning/**

A single-page, offline-capable web app that turns a neural network diagram into a **live calculator**. Unlike static diagram tools, every value is computed in real time as you edit it.

### Features
- **Weight labels on every edge** — `w₁₁, w₂₁, w₃₁ …` using the standard `w_{jk}` convention (into neuron *j*, from neuron *k*), colour-coded by sign (blue = +, red = −) and width ∝ |weight|.
- **`z` and `σ(z)` inside each neuron** — see the pre-activation and the activation together.
- **Live forward pass** — click any input, weight, or bias to edit it; the whole network recomputes instantly.
- **Separate hidden vs. output activation** — sigmoid / tanh / ReLU for hidden layers; sigmoid / softmax / linear (regression) for the output.
- **Hover a neuron** to expand its full equation with real numbers.
- **Animate** the forward pass layer-by-layer, **randomize weights**, and **export the diagram as SVG** for slides.

### How students use it
1. Open the link above in any modern browser (Chrome, Edge, Firefox, Safari). No installation, no login.
2. Change the architecture (e.g. `2,3,1`), type input values, and watch the math flow through the network.

### Run locally (optional)
Just open `index.html` in a browser — it is fully self-contained (no dependencies, no build step).

---

## 📚 Course Materials

Hands-on Jupyter notebooks and lecture slides. Every notebook in the two featured series below
was **executed**, so the plots, comparison tables, and metrics render directly on GitHub.

### 1. `notebooks_DeepLearning/` — Neural-network training techniques (Keras **and** PyTorch)
A paired series on the **loan-prediction** dataset: the *same* concept implemented once in Keras
and once in PyTorch, side by side. Covers baselines (with confusion matrix / ROC-AUC), optimizers,
weight initialization, early stopping, gradient clipping, batch normalization, dropout,
model save/load, a combined comparison, **learning-rate schedules**, and **hyperparameter search**.
→ see [`notebooks_DeepLearning/README.md`](notebooks_DeepLearning/README.md).

### 2. `notebooks_RNN_LSTM/` — RNN & LSTM concepts (Keras)
A concept-centric series where **each notebook teaches one recurrent-network idea on two datasets**
at once — **IMDB** sentiment (text classification) and **Jena Climate** weather (time-series
forecasting). Covers sequence data prep, SimpleRNN, LSTM, GRU, stacked/deep RNNs, bidirectional
layers, dropout/`recurrent_dropout`, a 4-way model comparison, save/load, and dataset-specific
advanced topics (embeddings & masking; multivariate & multi-step forecasting).
→ see [`notebooks_RNN_LSTM/README.md`](notebooks_RNN_LSTM/README.md).

### 3. `notebooks/` — Standalone lecture notebooks
Individual teaching notebooks used across the sessions (backpropagation from scratch,
batch/mini-batch/SGD, SGD-with-momentum from scratch, optimizers on MNIST, grid search,
CNN filters, and more). → see [`notebooks/README.md`](notebooks/README.md).

### 4. `slides/` — Lecture slides & course outline
PowerPoint decks and the course outline PDF. → see [`slides/README.md`](slides/README.md).

### 5. Large downloads (Releases)
Files too large for the git tree (>100 MB) are published as **release assets** on the
[**Releases page**](https://github.com/mlnjsh/Introduction-to-Deep-Learning/releases/tag/v1.0):
- `Session_01.pptx` (~147 MB) — full Session 1 lecture deck.
- `best_model.keras` (~172 MB) — a saved trained Keras model checkpoint (batch-norm notebook).

### Datasets at the repo root
- `loan_prediction_data.csv` — pre-normalized loan-approval data used by `notebooks_DeepLearning/`.
- `housing.data.txt` — Boston-housing data used by some standalone notebooks.

---

## 🌐 Curated Resources

A companion reading list — the best **YouTube channels** (StatQuest, 3Blue1Brown, Luis Serrano,
Karpathy…), **free books**, **interactive visualization tools**, **Kaggle** learning tracks &
case studies, **landmark papers**, and **industry research blogs** (Google, DeepMind, Meta,
Netflix, OpenAI, Anthropic). → see [**`RESOURCES.md`**](RESOURCES.md).

---

## Environment

The featured notebooks were run on TensorFlow 2.21 + PyTorch 2.11 (CPU). To run them:

```bash
pip install tensorflow torch scikit-learn pandas matplotlib truststore
```

Then open a notebook and run top-to-bottom. For the RNN/LSTM series, run
`notebooks_RNN_LSTM/01_sequence_data_prep.ipynb` first — it downloads and caches IMDB and Jena.

---
© Dr. Milan Joshi · MathCanvasMJ. For educational use.
