from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"

def generate_ai(prompt, system_role):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/campaign")
def campaign():
    return render_template("campaign.html")

@app.route("/pitch")
def pitch():
    return render_template("pitch.html")

@app.route("/leads")
def leads():
    return render_template("leads.html")

@app.route("/insights")
def insights():
    return render_template("insights.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["input"]
    mode = request.form["mode"]

    system_prompts = {
        "campaign": "Generate structured campaign strategy.",
        "pitch": "Generate persuasive structured sales pitch.",
        "leads": "Provide structured predictive lead scoring model.",
        "insights": "Provide executive business insights with data-driven analysis."
    }

    result = generate_ai(prompt, system_prompts.get(mode))
    return jsonify({"response": result})

@app.route("/")
def home():
    return render_template("dashboard.html")


if __name__ == "__main__":
    print(app.url_map)   # optional debug
    app.run(debug=True)   
print(app.url_map)
