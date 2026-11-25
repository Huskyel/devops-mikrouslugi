import os
from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "dev")

@app.route("/")
def home():
    return f"Aplikacja dziala! Wersja: {APP_VERSION}"

@app.route("/status")
def status():
    return jsonify({"status": "ok", "version": APP_VERSION, "service": "mikrousluga-demo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
