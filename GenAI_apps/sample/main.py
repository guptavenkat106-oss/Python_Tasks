import os
from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key="AIzaSyCUvci7F_ztB-Dw3a48-G40QKNFJMXDnJo"
)
def summarize_text(text):
    prompt = f"Summarize the following text in simple words:\n\n{text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# Main program
if __name__ == "__main__":
    print("=== AI Text Summarizer ===\n")

    user_text = input("Enter long text:\n\n")

    summary = summarize_text(user_text)

    print("\n=== Summary ===\n")
    print(summary)