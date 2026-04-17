
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

HEADLINES = [
    "Virat Kohli dances with a dog at India Gate after scoring century in dreams",
    "Bollywood star buys auto-rickshaw to avoid paparazzi, becomes full-time driver",
    "Indian politician promises free WiFi to cows for Digital India phase 2",
    "MS Dhoni spotted giving helicopter shot lessons to street lights",
    "Amitabh Bachchan replaces Google Maps with his own voice directions",
    "Cricketers demand tea break every 5 overs to feel at home",
    "Bollywood director casts traffic police as lead hero for realism",
    "Politician inaugurates same bridge for the 12th time with new ribbon color"
]

POPULAR = random.sample(HEADLINES, 3)

@app.route("/")
def index():
    return render_template("index.html", popular=POPULAR)

@app.route("/generate")
def generate():
    return jsonify({"headline": random.choice(HEADLINES)})

if __name__ == "__main__":
    app.run(debug=True)
