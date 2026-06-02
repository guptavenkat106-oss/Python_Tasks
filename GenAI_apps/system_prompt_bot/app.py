from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

API_KEY = "AQ.Ab8RN6K_Vi-9GO8bcC8k5YyNXHRpz6t99fUHBp3H5zaLPB3X0Q"

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Create a .env file and add:\n"
        "GEMINI_API_KEY=your_api_key_here"
    )

# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(title="GenAI System Prompt Bot")

# ============================================================
# Request Model
# ============================================================

class QuestionRequest(BaseModel):
    question: str

# ============================================================
# Classifier
# ============================================================

def is_python_related(question: str) -> bool:

    prompt = f"""
You are a strict classifier.

Return ONLY YES or NO.

Return YES only if the question is clearly related to:
- Python Programming
- Java Programming
- FastAPI
- Flask
- AI/ML
- GenAI

Return NO for:
- Greetings
- Random text
- Personal conversation
- Non-technical topics

Question:
{question}

Answer:
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text.strip().upper() == "YES"

    except Exception:
        return False

# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():
    return {
        "message": "GenAI API Running Successfully"
    }

# ============================================================
# Ask Route
# ============================================================

@app.post("/ask")
def ask_question(data: QuestionRequest):

    question = data.question

    if not is_python_related(question):
        return {
            "answer": (
                "⚠️ This assistant only supports "
                "Python, Java, FastAPI, Flask, AI/ML and GenAI questions."
            )
        }

    system_prompt = """
You are an AI learning assistant.

Rules:
- Be beginner friendly.
- Give structured answers.
- Give examples when needed.
- Keep answers clear and concise.
"""

    full_prompt = f"""
{system_prompt}

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt
        )

        return {
            "answer": response.text
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}"
        }