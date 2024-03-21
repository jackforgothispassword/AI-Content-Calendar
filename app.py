from flask import Flask, render_template, request
import os
from openai import OpenAI

# Instantiate the Flask app
app = Flask(__name__)

# Instantiate the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_video_ideas():
    prompt = "Generate video content ideas for a YouTube channel about personal development."

    # Generate ideas using OpenAI API
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Recommended replacement
        prompt=prompt,
        max_tokens=100
    )

    ideas = completion.choices[0].text.strip().split('\n')
    return ideas

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        video_ideas = generate_video_ideas()
        return render_template('index.html', video_ideas=video_ideas)
    else:
        return render_template('index.html', video_ideas=None)

if __name__ == "__main__":
    app.run(debug=True)
