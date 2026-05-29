from fastapi import FastAPI
from google import genai

# Create FastAPI app
app = FastAPI()

# Gemini Client
client = genai.Client(
    api_key="AQ.Ab8RN6KyO7KGIrat8-kAfW17TSQNSW6nLGB0JL5Qlt3Bn26CUQ"
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Gemini AI API Running Successfully"
    }

# AI Route
@app.get("/ask")
def ask_ai(question: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return {
            "question": question,
            "answer": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }