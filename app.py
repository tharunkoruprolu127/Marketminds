from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def generate_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert AI Sales & Marketing Strategist.
Provide structured professional output with headings and bullet points."""
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {str(e)}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/campaign', methods=['POST'])
def campaign():
    product = request.form.get('product')
    target = request.form.get('target')

    if not product or not target:
        return render_template('campaign.html', result="Please provide all inputs.")

    prompt = f"""
    Create a complete marketing campaign for:
    Product: {product}
    Target Audience: {target}

    Include:
    - Campaign theme
    - Social media strategy
    - Email marketing plan
    - Tagline
    """

    result = generate_ai_response(prompt)

    return render_template('campaign.html', result=result)


@app.route('/pitch', methods=['POST'])
def pitch():
    product = request.form.get('product')
    audience = request.form.get('audience')

    if not product or not audience:
        return render_template('pitch.html', result="Please provide all inputs.")

    prompt = f"""
    Create a persuasive sales pitch for:
    Product: {product}
    Audience: {audience}

    Include:
    - Value proposition
    - Pain points
    - Benefits
    - Closing statement
    """

    result = generate_ai_response(prompt)

    return render_template('pitch.html', result=result)


@app.route('/lead', methods=['POST'])
def lead():
    industry = request.form.get('industry')
    behavior = request.form.get('behavior')

    if not industry or not behavior:
        return render_template('lead.html', result="Please provide all inputs.")

    prompt = f"""
    Analyze this lead:

    Industry: {industry}
    Behavior: {behavior}

    Provide:
    - Lead Score (1-100)
    - Reasoning
    - Recommended action
    """

    result = generate_ai_response(prompt)

    return render_template('lead.html', result=result)


@app.route('/insights', methods=['POST'])
def insights():
    market = request.form.get('market')

    if not market:
        return render_template('insights.html', result="Please provide market sector.")

    prompt = f"""
    Provide detailed market analysis for:
    {market}

    Include:
    - Market trends
    - Opportunities
    - Risks
    - Competitive landscape
    - Strategic recommendations
    """

    result = generate_ai_response(prompt)

    return render_template('insights.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)