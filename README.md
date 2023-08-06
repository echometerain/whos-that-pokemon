---
title: Who's That Pokemon?
emoji: ⚡
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 3.38.0
app_file: app.py
pinned: false
---

# Who's That Pokemon?

[Kaggle link](https://www.kaggle.com/code/echometerhhwl/who-s-that-pokemon-improved) | [Huggingface demo](https://huggingface.co/spaces/echometerain/whos-that-pokemon)

Identifies generation 1 pokemon based on [35627 images](https://www.kaggle.com/datasets/echometerhhwl/pokemon-gen-1-38914)!

![image](https://github.com/echometerain/whos-that-pokemon/assets/70437021/68b0ed63-4be6-4d30-a06f-a8c1b59060a3)

![image](https://github.com/echometerain/whos-that-pokemon/assets/70437021/e46821ee-26ce-4976-8545-da8786fdc9c0)

Default model based on convnext_tiny (`model.pkl`) has 95.7% accuracy (with dataset augmented at runtime)

![image](https://github.com/echometerain/whos-that-pokemon/assets/70437021/b3006352-ad07-4227-9da3-aa9c182d3303)

Alternative model based on resnet34 (`model-r34.pkl`) has 94.3% accuracy (with dataset augmented at runtime)

![image](https://github.com/echometerain/whos-that-pokemon/assets/70437021/5e41262e-86b9-4dde-a48a-56951ea25644)
