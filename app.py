from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

# Configure API keys
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING_V2"] = "true"

# Prompt and model setup
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to {language}."),
    ("human", "{input}")
])

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_output_tokens=100,
    top_p=0.95,
    top_k=40,
)

output_parser = StrOutputParser()
llm_chain = prompt | model | output_parser

@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()
        input_text = data.get("input")
        language = data.get("language")

        if not input_text or not language:
            return jsonify({"error": "Missing input or language"}), 400

        response = llm_chain.invoke({
            "input": input_text,
            "language": language
        })

        return jsonify({"translation": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
