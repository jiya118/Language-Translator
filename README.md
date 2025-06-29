# 🌍 LLM-Powered Language Translator App

A lightweight, intelligent language translator app built using **Flask**, **LangChain**, and **Gemini 1.5 Flash**. This project demonstrates how to use LLMs to translate English into any target language using just a few lines of code.

## 🚀 Features

- Translate from English to any language (supports all languages supported by Gemini)
- Built using Google’s Gemini 1.5 Flash model via LangChain
- Clean, user-friendly web interface
- Lightweight Flask backend
- CORS-enabled for easy API integration

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **LangChain**
- **Google Generative AI (Gemini 1.5 Flash)**
- **HTML/CSS** (basic frontend)
- **.env** for secure API key handling

## 🖥️ How It Works

1. User inputs text and selects the target language
2. App sends this input to a LangChain prompt using Gemini
3. LLM returns a translated version, which is displayed on the frontend

## ⚙️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/llm-translator-app.git
   cd llm-translator-app

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Set up your .env file:**
   
    Create '.env' file containing your API keys -
   
     GOOGLE_API_KEY=your_google_api_key </br>
     LANGCHAIN_API_KEY=your_langchain_api_key 
   
    You'll need: </br>
    -Google Generative AI API Key (get it from Google AI Studio) </br>
    -LangChain API Key (for LangSmith/tracing)

5. **Run the App:**
   ```bash
   python app.py or flask run
   ```
   Follow the link to your localhost. 


 ## 📂 File Structure
├── app.py </br>
├── templates/ </br>
│      └── index.html </br>
├── static/ </br>
│      └── styles.css </br>
│      └── scripts.js </br>
├── .env </br>
└── requirements.txt </br>


## 🧠 Example 
**Input:**</br>
"How are you today?"

**Target Language:** Spanish

**Output:**</br>
"¿Cómo estás hoy?"
