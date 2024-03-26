def generate_video_ideas(niche, target_audience, content_type, tone_style, unique_twist):
    prompt = f"""Generate 10 YouTube video content ideas for a channel about {niche}, 
targeted at {target_audience}, focusing on {content_type} videos. 
The tone should be {tone_style}, and the content should include {unique_twist}. 
Additionally, suggest 5 example YouTubers to research for the proposed niche."""

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
        content_type = request.form.get('content_type')
        tone_style = request.form.get('tone_style')
        unique_twist = request.form.get('unique_twist')

        video_ideas = generate_video_ideas(niche, target_audience, content_type, tone_style, unique_twist)
        return render_template('index.html', video_ideas=video_ideas, niche=niche)
    else:
        return render_template('index.html', video_ideas=None)
