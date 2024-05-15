<p align="center">
    <img src="https://github.com/austinlackey/llama-3-NPS/blob/main/DALLE%20LLama.png" width="500">
</p>

# Fine-tuning Llama-3-8B for extracting information from NPS comments

### Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

# Motivation
The VU Statistics program within the National Park Service (NPS) is responsible for maintaining and analyzing visitor data across the entire NPS system. All ~420 NPS units collect visitor data, and leave free-form comments that describe the visitation patterns for a given month. Going through these comments can be a time-consuming process, and LLMs have the nuance to understand the context of the comments and extract the information that is relevant to the VU Statistics program.

# :sparkles: Innovative Emphasis
**LLMs often have a barrier to entry, either due to the computational resources required, or the money needed to access APIs. Both open-source models, and modern QLoRA techniques can be used to fine-tune LLMs for specific use-cases on the local level. This allows for the democratization of LLMs, and the ability to fine-tune a model that works best for National Park Service data.**

# Methodology
My methodology for this project is explained in detail in the following 
[Medium article]()

# I/O Example
![I/O Example](https://github.com/austinlackey/llama-3-NPS/blob/main/Visuals/OutputExample.png)
Fine-tuning Llama-3-8B for extracting closure-related information from long/verbose NPS comments.