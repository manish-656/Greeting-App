from flask import Flask, render_template, request
import random

app = Flask(__name__)

QUOTES = [
    "🌟 Believe you can and you're halfway there!",
    "💪 Push yourself, because no one else is going to do it for you.",
    "🌈 Keep shining, the world needs your light!",
    "🚀 Dream big and dare to fail.",
    "😊 Happiness is not by chance, but by choice.",
    "🔥 Don’t watch the clock; do what it does. Keep going!",
    "🌻 Every day is a second chance.",
    "🌊 Go with the flow, but always keep your goals in mind.",
    "✨ You are stronger than you think.",
    "🌎 Be the change that you wish to see in the world.",
    "🍀 Good things are coming, keep believing.",
    "☀️ Rise up and attack the day with enthusiasm.",
    "🌹 Difficulties in life don’t come to destroy you, but to help you realize your hidden potential.",
    "🦋 Change is beautiful, just like you.",
    "🎯 Stay focused, stay positive, stay strong.",
    "🌟 Make today so awesome that yesterday gets jealous."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username', '').strip()
    if not name:
        name = "Friend"
    quote = random.choice(QUOTES)
    return render_template('greet.html', name=name, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
