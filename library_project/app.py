from flask import Flask, render_template
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000"

@app.route("/")
def home():

    response = requests.get(
        f"{FASTAPI_URL}/books"
    )

    books = response.json()

    return render_template(
        "index.html",
        books=books
    )

if __name__ == "__main__":

    app.run(debug=True)