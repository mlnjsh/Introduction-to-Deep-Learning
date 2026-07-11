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

## 🔁 Neural Network Backward-Pass (Backprop) Visualizer

**▶ Open it live: https://mlnjsh.github.io/Introduction-to-Deep-Learning/backprop.html**

The companion to the forward-pass tool — it shows **how the weights get updated**. Watch the
gradient flow *backward* through the network and see every chain-rule step, for **both** problem
types students meet first: **binary classification** (sigmoid + BCE) and **regression** (linear +
MSE).

### Features
- **Every neuron shows two numbers** — `a` = its activation (forward, teal) and **`δ = ∂L/∂z`** (backward, orange).
- **Full chain-rule derivation on hover** — hover a hidden neuron to expand
  `δ = (Σ wᵢⱼ·δᵢ) · σ′(z)` with real numbers; hover an edge to see
  `∂L/∂w = δ·a` and the update `w_new = w − η·∂L/∂w`.
- **The "aha" simplification made visible** — for both sigmoid+BCE and linear+MSE, the output error
  collapses to the same clean **`δ = ŷ − y`**, shown explicitly.
- **Take a gradient step** (or run 10) and watch the **loss fall live** in the bottom bar.
- **Edge-label modes** — show the weight `w`, its gradient `∂L/∂w`, or the update `Δw`.
- **Animate the backward pass** layer-by-layer, edit any input/target/learning-rate, and export the diagram as SVG.
- Gradients are **numerically verified** against finite differences, so what you see is exactly correct.

### How students use it
1. Open the link above (or `backprop.html` locally — fully self-contained).
2. Pick a problem type, set the target `y`, hover neurons/edges to read the formulas, then press
   **Take gradient step** and watch `δ`, the weights, and the loss all change together.

---

## 🧪 Neural Lab — Interactive Deep Learning Playground

**▶ Open it live: https://neural-lab.replit.app**

A full **build-train-and-watch** playground that goes beyond a single forward/backward pass. Design a
network, generate a dataset, and train it live — all in the browser.

### What you can do
- **Compose an architecture** — add fully-connected layers and set the **units** and **activation**
  (ReLU / Sigmoid / …) for each, with a live layer diagram (`Input → Hidden → Output`).
- **Pick the training recipe** — choose the **loss function** (e.g. Binary Cross-Entropy) and the
  **optimizer** (e.g. Adam).
- **Train on 2-D data** — watch **Training Data & Predictions** update as the decision boundary forms.
- **See the Loss Landscape** — visualize `L(W₁, W₂)` as a **contour map or a 3-D surface**, so students
  see *what* gradient descent is actually descending.
- **Step-by-step** — a step counter and light/dark mode; everything runs client-side, nothing to install.

> Hosted on Replit. It complements the two SVG visualizers above: the Forward/Backward tools zoom in on
> the math of one pass; **Neural Lab** zooms out to the full training loop and loss surface.

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
