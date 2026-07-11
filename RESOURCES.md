# 📖 Curated Deep Learning Resources

A hand-picked companion to the *Introduction to Deep Learning* course — the channels, books,
interactive tools, datasets, landmark papers, and industry blogs I actually recommend to students.
Start with the **⭐ starred** items in each section; they are the highest-signal places to begin.

> Maintained by **Dr. Milan Joshi** (MathCanvasMJ). Suggestions welcome via an issue or PR.

---

## 🎬 YouTube Channels

### Intuition & visual explanations (best for beginners)
- ⭐ **3Blue1Brown** — the *Neural Networks* series is the gold standard for visual intuition (backprop, gradient descent, transformers). https://www.youtube.com/@3blue1brown
- ⭐ **StatQuest with Josh Starmer** — "clearly explained" ML/DL from the ground up; superb on the math without the pain. https://www.youtube.com/@statquest
- ⭐ **Serrano.Academy (Luis Serrano)** — friendly, geometry-first explanations of neural nets, attention, and generative models. https://www.youtube.com/@SerranoAcademy
- **Computerphile** — short, deep single-topic explainers with researchers. https://www.youtube.com/@Computerphile
- **Artem Kirsanov** — beautifully animated neuroscience-meets-ML explainers. https://www.youtube.com/@ArtemKirsanov

### Coding & building models
- ⭐ **Andrej Karpathy** — *Neural Networks: Zero to Hero*; build GPT/backprop from scratch, line by line. https://www.youtube.com/@AndrejKarpathy
- **freeCodeCamp** — long, free full-course tutorials (TensorFlow, PyTorch, ML). https://www.youtube.com/@freecodecamp
- **sentdex** — practical Python + deep learning projects. https://www.youtube.com/@sentdex
- **Nicholas Renotte** — end-to-end applied DL/CV/NLP builds. https://www.youtube.com/@NicholasRenotte
- **Aladdin Persson** — clean PyTorch/TensorFlow implementations of papers. https://www.youtube.com/@AladdinPersson

### Research, papers & staying current
- ⭐ **Yannic Kilcher** — thorough paper walkthroughs of the latest research. https://www.youtube.com/@YannicKilcher
- **Two Minute Papers** — bite-sized "what just got published and why it's cool." https://www.youtube.com/@TwoMinutePapers
- **The AI Epiphany (Aleksa Gordić)** — deep code + paper deep-dives. https://www.youtube.com/@TheAIEpiphany
- **DeepLearningAI (Andrew Ng)** — talks, The Batch, short courses. https://www.youtube.com/@Deeplearningai
- **Lex Fridman** — long-form interviews with the field's leaders. https://www.youtube.com/@lexfridman

---

## 📚 Books (with free/official links)

### Free & online
- ⭐ **Dive into Deep Learning (D2L)** — interactive, code-first (PyTorch/TF/JAX), used at 500+ universities. https://d2l.ai
- ⭐ **Neural Networks and Deep Learning** — Michael Nielsen; the clearest free intro to backprop. http://neuralnetworksanddeeplearning.com
- ⭐ **Understanding Deep Learning** — Simon Prince; modern, free PDF, gorgeous figures. https://udlbook.github.io/udlbook/
- **Deep Learning** — Goodfellow, Bengio, Courville; the classic "bible," free HTML. https://www.deeplearningbook.org
- **Probabilistic Machine Learning** — Kevin Murphy; two free volumes. https://probml.github.io/pml-book/
- **The Little Book of Deep Learning** — François Fleuret; a phone-sized free PDF. https://fleuret.org/francois/lbdl.html
- **Dive into Deep Learning** companion: **Mathematics for Machine Learning** (free). https://mml-book.github.io

### Highly recommended (paid)
- **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** — Aurélien Géron. Notebooks free: https://github.com/ageron/handson-ml3
- **Deep Learning with Python** — François Chollet (creator of Keras). Notebooks: https://github.com/fchollet/deep-learning-with-python-notebooks
- **Deep Learning for Coders with fastai & PyTorch** — Howard & Gugger. Free notebook version: https://github.com/fastai/fastbook
- **The Hundred-Page Machine Learning Book** — Andriy Burkov. https://themlbook.com

---

## 🧪 Interactive Visualization & Explainer Tools

- ⭐ **TensorFlow Playground** — train a tiny net in your browser; watch decision boundaries form. https://playground.tensorflow.org
- ⭐ **CNN Explainer** — interactively see how a convolutional net "sees" an image. https://poloclub.github.io/cnn-explainer/
- ⭐ **Transformer Explainer** — live, in-browser GPT-2 to demystify attention. https://poloclub.github.io/transformer-explainer/
- **The Illustrated Transformer** (Jay Alammar) — the canonical visual explainer of attention. https://jalammar.github.io/illustrated-transformer/
- **Netron** — drag-and-drop viewer for any model file (.keras/.onnx/.pt/.tflite). https://netron.app
- **Embedding Projector** — explore high-dimensional embeddings in 3D (PCA/t-SNE/UMAP). https://projector.tensorflow.org
- **Distill.pub** — interactive research articles; still the bar for ML explanation. https://distill.pub
- **Weights & Biases** — experiment tracking & live dashboards. https://wandb.ai · **TensorBoard** — https://www.tensorflow.org/tensorboard
- **ConvNetJS** (Karpathy) — deep learning entirely in the browser. https://cs.stanford.edu/people/karpathy/convnetjs/
- **Neural Network SVG generator (NN-SVG)** — publication-quality architecture diagrams. https://alexlenail.me/NN-SVG/
- **Your own repo's** [Forward-Pass Visualizer](https://mlnjsh.github.io/Introduction-to-Deep-Learning/) 😉

---

## 🏆 Kaggle — Learn, Datasets & Case Studies

- ⭐ **Kaggle Learn** — free, short, hands-on micro-courses (Intro to DL, Computer Vision, NLP). https://www.kaggle.com/learn
- **Datasets** — https://www.kaggle.com/datasets · **Competitions** — https://www.kaggle.com/competitions
- **Notebooks (Code)** — read top-voted public notebooks for real-world patterns. https://www.kaggle.com/code
- **Discussions & winning solution write-ups** — the best free "case studies" in applied DL. https://www.kaggle.com/discussions

**Classic learning competitions / case studies to study:**
- *Digit Recognizer (MNIST)* — CNN fundamentals. https://www.kaggle.com/c/digit-recognizer
- *Dogs vs. Cats* — transfer learning. https://www.kaggle.com/c/dogs-vs-cats
- *Titanic* — the ML "hello world" (tabular). https://www.kaggle.com/c/titanic
- *House Prices* — regression end-to-end. https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- Browse **"winning solutions" write-ups** on any past competition's Discussion tab — grandmasters document their full pipelines.

---

## 🗂️ Datasets (by problem type)

Every dataset below is tagged with **the kind of ML problem it poses** so you can pick the right one
for the concept you're teaching. *Classification* = predict a category; *Regression* = predict a
number; *Forecasting* = predict future values of a sequence (a regression over time).

### Tabular — for MLP / dense-network basics
| Dataset | Problem type | Notes |
|---|---|---|
| **Iris** | Multiclass classification (3 classes) | The "hello world" of ML; 4 features, 150 rows. |
| **Titanic** | Binary classification (survived?) | Great for feature engineering. https://www.kaggle.com/c/titanic |
| **Breast Cancer Wisconsin** | Binary classification (malignant/benign) | Built into scikit-learn. |
| **Adult / Census Income** | Binary classification (>50K?) | Class imbalance + categorical features. |
| **California Housing** | **Regression** (median house value) | Modern replacement for Boston Housing; in scikit-learn. |
| **Wine Quality** | Regression *or* classification (score 0–10) | Shows how one dataset frames both. |
| **Bike Sharing / Auto MPG** | **Regression** (count / mpg) | Clean small regression sets. |
| **`loan_prediction_data.csv`** (this repo) | Binary classification (approve loan?) | Used by `notebooks_DeepLearning/`. |

### Images — for CNNs
| Dataset | Problem type | Notes |
|---|---|---|
| **MNIST** | Multiclass classification (10 digits) | 28×28 grayscale; the CNN starter. |
| **Fashion-MNIST** | Multiclass classification (10 clothes) | Drop-in, harder than MNIST. |
| **CIFAR-10 / CIFAR-100** | Multiclass classification (10 / 100) | 32×32 colour; real CNN benchmark. |
| **Cats vs Dogs** | Binary classification | Transfer-learning classic. https://www.kaggle.com/c/dogs-vs-cats |
| **Oxford Flowers-102 / Food-101** | Fine-grained classification | Good for augmentation & transfer learning. |
| **ImageNet (ILSVRC)** | Multiclass classification (1000) | The large-scale benchmark. https://www.image-net.org |

### Text & sequences — for RNN / LSTM / GRU (the focus of `notebooks_RNN_LSTM/`)
| Dataset | Problem type | RNN framing |
|---|---|---|
| ⭐ **IMDB movie reviews** | Binary **classification** (sentiment) | many-to-one: Embedding → RNN → sigmoid. *Used in this repo.* |
| **AG News** | Multiclass classification (4 topics) | many-to-one text classification. |
| **Reuters-21578 / 20 Newsgroups** | Multiclass classification | topic labelling from a document. |
| **SST-2 / Yelp / Amazon reviews** | Binary/ordinal classification | sentiment; ordinal = "regression-ish" on stars. |
| **SNLI / MultiNLI** | Classification (entail/contradict/neutral) | pair-of-sequences classification. |
| **Penn Treebank (PTB) / WikiText-2** | **Language modeling** (next-word) | many-to-many self-supervised; predicts a distribution. |
| **Multi30k / WMT / Tatoeba** | **Seq2seq** (translation) | encoder–decoder, many-to-many. |
| **Names → language** (PyTorch tutorial) | Char-level classification | tiny, perfect for teaching char-RNNs. |

### Time series — for RNN/LSTM **forecasting** (a regression over time)
| Dataset | Problem type | Notes |
|---|---|---|
| ⭐ **Jena Climate** | **Forecasting / regression** (temperature) | sliding-window; multivariate. *Used in this repo.* |
| **Airline Passengers / Sunspots** | Univariate forecasting | the classic tiny time-series demos. |
| **Beijing PM2.5 Air Quality** | Forecasting / regression (pollution) | multivariate, missing values. |
| **UCI Household Power / Electricity Load** | Forecasting / regression (energy) | long, seasonal. |
| **M4 / M5 (Walmart)** | Forecasting (competition-grade) | thousands of series; the forecasting benchmark. |
| **Human Activity Recognition (HAR)** | Sequence **classification** (6 activities) | accelerometer windows → label. |
| **ECG5000 / UCR & UEA archives** | Sequence classification | 100+ labelled time-series datasets in one place. |

### Audio & speech — for 1-D CNNs / RNNs
- **Speech Commands** — keyword classification. · **UrbanSound8K** — sound classification. · **LibriSpeech** — speech-to-text (seq2seq).

### 🔎 Where to load them (dataset hubs)
- ⭐ **TensorFlow Datasets** (`tfds.load(...)`) — hundreds ready-to-stream. https://www.tensorflow.org/datasets/catalog/overview
- ⭐ **Hugging Face Datasets** (`load_dataset(...)`). https://huggingface.co/datasets
- ⭐ **UCI Machine Learning Repository** — the classic tabular/time-series source. https://archive.ics.uci.edu
- **Built into the frameworks** — `keras.datasets`, `torchvision`, `torchtext`, `torchaudio`, `sklearn.datasets`.
- **Kaggle Datasets** https://www.kaggle.com/datasets · **OpenML** https://www.openml.org
- **Papers with Code — Datasets** (filter by task). https://paperswithcode.com/datasets
- **Time-series specialists:** **UCR/UEA archive** (classification) https://www.timeseriesclassification.com · **Monash Forecasting Repository** https://forecastingdata.org

---

## 🎓 Full Courses (free)

- ⭐ **fast.ai — Practical Deep Learning for Coders** — top-down, code-first, world-class. https://course.fast.ai
- ⭐ **DeepLearning.AI — Deep Learning Specialization** (Andrew Ng). https://www.coursera.org/specializations/deep-learning
- **Stanford CS231n — CNNs for Visual Recognition**. https://cs231n.github.io
- **Stanford CS224n — NLP with Deep Learning**. https://web.stanford.edu/class/cs224n/
- **MIT 6.S191 — Introduction to Deep Learning** (yearly, videos + labs). https://introtodeeplearning.com
- **Hugging Face Courses** — NLP, Deep RL, Diffusion, Agents. https://huggingface.co/learn

---

## 📄 Landmark Papers (foundations, with arXiv links)

Read these in roughly this order to build the modern DL story:

| Paper | Year | arXiv |
|---|---|---|
| Adam: A Method for Stochastic Optimization | 2014 | https://arxiv.org/abs/1412.6980 |
| Dropout | 2014 | https://jmlr.org/papers/v15/srivastava14a.html |
| Batch Normalization | 2015 | https://arxiv.org/abs/1502.03167 |
| Deep Residual Learning (ResNet) | 2015 | https://arxiv.org/abs/1512.03385 |
| Generative Adversarial Networks (GANs) | 2014 | https://arxiv.org/abs/1406.2661 |
| Attention Is All You Need (Transformer) | 2017 | https://arxiv.org/abs/1706.03762 |
| BERT | 2018 | https://arxiv.org/abs/1810.04805 |
| An Image is Worth 16x16 Words (ViT) | 2020 | https://arxiv.org/abs/2010.11929 |
| Denoising Diffusion Probabilistic Models (DDPM) | 2020 | https://arxiv.org/abs/2006.11239 |
| GPT-3 (Language Models are Few-Shot Learners) | 2020 | https://arxiv.org/abs/2005.14165 |
| LoRA: Low-Rank Adaptation | 2021 | https://arxiv.org/abs/2106.09685 |
| Chinchilla (Training-Compute-Optimal LLMs) | 2022 | https://arxiv.org/abs/2203.15556 |
| LLaMA: Open & Efficient Foundation Models | 2023 | https://arxiv.org/abs/2302.13971 |

---

## 🔬 Staying Current with Ongoing Research

These are **living feeds** — bookmark them instead of chasing individual links:

- ⭐ **arXiv** — the source. Daily new work: [cs.LG](https://arxiv.org/list/cs.LG/recent) · [cs.CV](https://arxiv.org/list/cs.CV/recent) · [cs.CL](https://arxiv.org/list/cs.CL/recent)
- ⭐ **Papers with Code** — papers *with* runnable code + leaderboards + SOTA tables. https://paperswithcode.com
- ⭐ **Hugging Face Papers** — daily community-curated top papers. https://huggingface.co/papers
- **Semantic Scholar** — AI-powered literature search & citation graphs. https://www.semanticscholar.org
- **Google Scholar** — set alerts for authors/keywords. https://scholar.google.com
- **The Batch** (DeepLearning.AI) — weekly newsletter that filters the noise. https://www.deeplearning.ai/the-batch/
- **Import AI** (Jack Clark) — weekly policy + research digest. https://importai.substack.com

---

## 🏢 Industry Research Blogs & Tech Blogs

### AI labs
- ⭐ **OpenAI — Research** https://openai.com/research · **News** https://openai.com/news
- ⭐ **Anthropic — Research** https://www.anthropic.com/research · **News** https://www.anthropic.com/news · **Engineering** https://www.anthropic.com/engineering
- ⭐ **Google Research** https://research.google/blog/ · **Google DeepMind** https://deepmind.google/discover/blog/
- ⭐ **Meta AI (FAIR)** https://ai.meta.com/blog/
- **Microsoft Research** https://www.microsoft.com/en-us/research/blog/
- **NVIDIA Developer / Research** https://developer.nvidia.com/blog/ · https://www.nvidia.com/en-us/research/
- **Hugging Face Blog** https://huggingface.co/blog

### Engineering / applied-ML in production ("case studies")
- ⭐ **Netflix Technology Blog** — recommendation systems & ML at scale. https://netflixtechblog.com
- **Meta Engineering** https://engineering.fb.com · **Uber Engineering** https://www.uber.com/en-US/blog/engineering/
- **Spotify Engineering** https://engineering.atspotify.com · **Airbnb Tech** https://medium.com/airbnb-engineering
- **Amazon Science** https://www.amazon.science/blog · **Apple Machine Learning Research** https://machinelearning.apple.com

### Independent researcher blogs (exceptional teaching)
- ⭐ **Lil'Log (Lilian Weng)** — deep, rigorous surveys (attention, diffusion, agents). https://lilianweng.github.io
- ⭐ **Jay Alammar** — "Illustrated" everything (Transformer, BERT, GPT). https://jalammar.github.io
- **Andrej Karpathy** https://karpathy.github.io · **Sebastian Ruder (NLP)** https://www.ruder.io
- **Chris Olah** https://colah.github.io · **Chip Huyen (ML systems)** https://huyenchip.com/blog/
- **Sebastian Raschka — Ahead of AI** https://magazine.sebastianraschka.com

---

## 🛠️ Cheat Sheets & Quick References
- **Stanford CS230 DL cheatsheets** — https://stanford.edu/~shervine/teaching/cs-230/
- **PyTorch docs & tutorials** — https://pytorch.org/tutorials/ · **Keras guides** — https://keras.io/guides/
- **scikit-learn user guide** — https://scikit-learn.org/stable/user_guide.html

---
© Dr. Milan Joshi · MathCanvasMJ. Curated for educational use — links point to the original authors and owners.
