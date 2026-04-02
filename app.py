import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"quote": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"quote": "You miss 100% of the shots you don't take.", "author": "Wayne Gretzky"},
    {"quote": "Whether you think you can or you think you can't, you're right.", "author": "Henry Ford"},
    {"quote": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"quote": "An unexamined life is not worth living.", "author": "Socrates"},
    {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
]


@app.route("/quote", methods=["GET"])
def get_quote():
    quote = random.choice(QUOTES)
    return jsonify({
        "quote": quote["quote"],
        "author": quote["author"],
        "status": "success"
    }), 200


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "quoteapi",
        "version": "0.1.0"
    }), 200


@app.route("/quotes", methods=["GET"])
def get_all_quotes():
    return jsonify({
        "quotes": QUOTES,
        "total": len(QUOTES),
        "status": "success"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
