# import libraries
from flask import Flask, render_template, request
import os
from openai import OpenAI

#start flask app and set OpenAI API Key via .env
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Generate video ideas using prompt
def generate_video_ideas(niche, target_audience):
    prompt = f"Using knowledge of YouTube and successful videos on the platform, generate 10 video content ideas for a YouTube channel about the {niche} niche, for the target audience of {target_audience}. Then add a new section with 5 example YouTubers to research for the proposed niche. Do not number the ideas in your output."

    # Specify model
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000
    )

    ideas = completion.choices[0].text.strip().split('\n')
    return ideas

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        niche = request.form.get('niche')
        target_audience = request.form.get('target_audience')
        video_ideas = generate_video_ideas(niche, target_audience)
        return render_template('index.html', video_ideas=video_ideas, niche=niche, target_audience=target_audience)
    else:
        return render_template('index.html', video_ideas=None)

if __name__ == "__main__":
    app.run(debug=True)
