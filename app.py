from flask import Flask, render_template, request
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_video_ideas(niche):
    prompt = f"Generate video content ideas for a YouTube channel about {niche}."

    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )

    ideas = completion.choices[0].text.strip().split('\n')
    return ideas

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        niche = request.form.get('niche')
        video_ideas = generate_video_ideas(niche)
        return render_template('index.html', video_ideas=video_ideas, niche=niche)
    else:
        return render_template('index.html', video_ideas=None)

if __name__ == "__main__":
    app.run(debug=True)
