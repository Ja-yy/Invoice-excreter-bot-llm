# Invoice-excreter-bot-llm

### 📄Project description

Welcome to my Streamlit app designed for invoice extraction utilizing OpenAI's API. This versatile tool offers two distinct output models for enhanced flexibility and accuracy in extracting invoice data.

### 🎯 Purpose and Achievement:

Acknowledging the widespread demand for data extraction solutions utilizing LLM, and inspired by Langchain's introduction of the `with_structured_output` method for enhanced model calls, I centered my efforts on tackling the common use case of invoice extraction, culminating in the development of this bot.

### ⚙️🚀 Technologies and Frameworks Utilized

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-black?style=for-the-badge)
![Langchain](https://img.shields.io/badge/%F0%9F%A6%9C%EF%B8%8F%F0%9F%94%97%20LangChain-black?style=for-the-badge)


### 💡Features

- Supports extraction of data from `PDF` files
- Utilizes `function calling` with LLM to enhance accuracy
- Offers two output options: `JSON` and `CSV`

### 🎬 Demo

https://github.com/Ja-yy/Invoice-excreter-bot-llm/assets/114324220/8d6be027-80c7-4a55-8b40-e3621066f4ac

### 🔜 Future Development and Features

In upcoming iterations, I aim to incorporate the ability to extract data from Excel and Word files, expanding the application's versatility and utility.

## ▶️ Run

Clone the repository

```bash
git clone git@github.com:Ja-yy/Invoice-excreter-bot-llm.git
```

Create a virtual environment using Pipenv:

```bash
pipenv install
```

Start Streamlit server:
```bash
streamlit run main.py 
```

Now, go to [localhost:8501](http://localhost:8501/)

Enjoy the app :)
