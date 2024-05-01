---

# Using Efficient Local Fine-tuning Techniques to Extract Closure Information From Long National Park Comments

## Overview
This repository contains the code, data, and paper for demonstrating the use of efficient local fine-tuning techniques to extract closure information from long national park comments. The project uses the Meta-Llama 3-8B model and the QLoRA fine-tuning technique to fine-tune the model on a dataset of national park comments. This codebase requires the cloning of the mlx repository for the fine-tuning scripts to utilize Apples CoreML framework for quantization and the QLoRA fine-tuning technique.

For more information, please refer to the paper in this repository.

## Files
In this repository, you will find the following files:

- `finetune.ipynb`: This notebook is used for formatting the data and fine-tuning the model. It also contains terminal commands at the end to train, run, and fuse the models.
- `main.ipynb`: Main notebook for loading and testing the models.
- `Visuals.Rmd`: R Markdown document for generating visualizations used in the paper. It includes code to visualize the data and results from the project.

## Download Models and Repos

Instructions on how to download, and run the models.

```ptyhon
# Download Llama directly from the Hugging Face model hub
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")
```

```bash
# Clone the mlx repository for the fine-tuning scripts
git clone https://github.com/ml-explore/mlx-examples
```

## Usage

Convert Model to Quantized Version:

```bash
# Quantize the model
python convert.py --hf-path <path-to-full-model> -q --mlx-path <path-to-save-quantized-model>
```

Fine-tune and Test the Model:

```bash
# Fine-tune the model
python lora.py --model <path-to-quantized-model> \
               --train \
               --data ../TrainData \
               --iters 1000 \
               --max-tokens 150 \
               --temp 0.3 \
               --batch-size 2 \
               --lora-layers 16
```

```bash
# Test the model
python lora.py --model <path-to-quantized-model> \
               --adapter-file ../Llama-3-adapters/adapters5.npz \
               --max-tokens 100 \
               --prompt "Input Prompt Here"
```

Fuse Final Adapter to Model:

```bash
# Fuse the final adapter to the model
python fuse.py --model <path-to-quantized-model> \
                --adapter-file ../Llama-3-adapters/adapters5.npz \
                --save-path <path-to-save-fused-model>
```
---