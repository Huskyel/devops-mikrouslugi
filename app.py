import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "dev")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

def get_redis():
    return redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.route("/")
def home():
    return f"Aplikacja dziala! Wersja: {APP_VERSION}"

@app.route("/status")
def status():
    return jsonify({"status": "ok", "version": APP_VERSION, "service": "mikrousluga-demo"})

@app.route("/odwiedziny")
def odwiedziny():
    try:
        count = get_redis().incr("licznik_odwiedzin")
        return jsonify({"odwiedziny": count, "version": APP_VERSION})
    except Exception as exc:
        return jsonify({"error": str(exc)}, status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
