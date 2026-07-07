# Introduction to Deep Learning

Interactive teaching tools for an *Introduction to Deep Learning* course, by **Dr. Milan Joshi** (MathCanvasMJ).

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
© Dr. Milan Joshi · MathCanvasMJ. For educational use.
