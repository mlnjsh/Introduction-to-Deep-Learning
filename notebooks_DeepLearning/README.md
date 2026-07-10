# Deep Learning Techniques — Keras vs PyTorch

A paired notebook series on the **loan prediction** dataset (`../loan_prediction_data.csv`,
614 applications, 11 pre-normalised features, binary target `Loan_Status`). Every topic has a
**Keras** notebook and a matching **PyTorch** notebook so you can compare the two frameworks
side by side. All notebooks are executed with real outputs, comparison tables, and
train-vs-test curves.

## Topics

| # | Topic | Keras | PyTorch | What you'll see |
|---|-------|-------|---------|-----------------|
| 01 | Simple baseline MLP | `01_baseline_keras.ipynb` | `01_baseline_pytorch.ipynb` | First model, train/test curve, **confusion matrix + ROC/AUC** |
| 02 | Optimizers | `02_optimizers_keras.ipynb` | `02_optimizers_pytorch.ipynb` | SGD / Momentum / RMSprop / Adam / Adagrad — table + overlaid curves |
| 03 | Weight initialization | `03_weight_init_keras.ipynb` | `03_weight_init_pytorch.ipynb` | Zeros / Random / Xavier / He — why zeros fails |
| 04 | Early stopping | `04_early_stopping_keras.ipynb` | `04_early_stopping_pytorch.ipynb` | Overfitting U-turn, patience, restore best weights |
| 05 | Gradient clipping | `05_grad_clipping_keras.ipynb` | `05_grad_clipping_pytorch.ipynb` | clipnorm vs clipvalue, training stability |
| 06 | Batch normalization | `06_batchnorm_keras.ipynb` | `06_batchnorm_pytorch.ipynb` | Faster convergence, train/eval mode |
| 07 | Dropout | `07_dropout_keras.ipynb` | `07_dropout_pytorch.ipynb` | Shrinking the train–test gap |
| 08 | Save / load model | `08_save_load_keras.ipynb` | `08_save_load_pytorch.ipynb` | `.keras`/weights/SavedModel vs `state_dict`/pickle/TorchScript |
| 09 | Final comparison | `09_comparison_keras.ipynb` | `09_comparison_pytorch.ipynb` | All techniques combined vs baseline |
| 10 | Learning-rate schedules | `10_lr_schedules_keras.ipynb` | `10_lr_schedules_pytorch.ipynb` | Constant/Step/Exp/Cosine/ReduceLROnPlateau — LR + loss curves (Keras also shows schedule *objects*) |
| 11 | Hyperparameter search | `11_hyperparameter_search_keras.ipynb` | `11_hyperparameter_search_pytorch.ipynb` | Grid (LR × batch, heatmap) + random search (log-uniform LR) |

## Framework mapping cheat-sheet

| Concept | Keras | PyTorch |
|---|---|---|
| Training | `model.fit(...)` | explicit `for` loop: `zero_grad → forward → backward → step` |
| Early stopping | `EarlyStopping` callback | hand-written loop + `copy.deepcopy(state_dict())` |
| Grad clip | `optimizer(clipnorm=...)` | `nn.utils.clip_grad_norm_` after `backward()` |
| Weight init | `kernel_initializer=` | `model.apply(...)` + `torch.nn.init.*` |
| He init | `"he_normal"` | `kaiming_normal_(..., nonlinearity="relu")` |
| Save (full) | `model.save("m.keras")` | `torch.save(model, ...)` |
| Save (weights) | `save_weights(".weights.h5")` | `torch.save(model.state_dict(), ...)` |
| Deploy format | `model.export()` (SavedModel) | `torch.jit.script(...)` (TorchScript) |
| Dropout/BN mode | automatic | `model.train()` / `model.eval()` |

## How to run

Open in Jupyter with the **`Python (DL course – TF 2.21)`** kernel (TensorFlow 2.21 +
PyTorch 2.11 both installed). Each notebook is self-contained — run top to bottom.

## Reading order

Follow the numbers 01 → 09. Read each Keras notebook first, then its PyTorch twin, to see
exactly what Keras automates under the hood.
