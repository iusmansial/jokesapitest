from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep!'"
]

@app.route('/api/joke')
def get_joke():
    return jsonify({'joke': random.choice(jokes)})

@app.route('/')
def home():
    return "<h1>Welcome to the Joke API</h1><p>Use /api/joke to get a joke!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
