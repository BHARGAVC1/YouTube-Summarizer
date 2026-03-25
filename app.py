import os
import json
from flask import Flask, render_template, request
from google import genai
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return None


def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return " ".join([t.text for t in transcript])
    except:
        return None


def generate_summary(content, extra_prompt):
    prompt = f"""
    Analyze the following content and return STRICTLY in JSON format:

    {{
      "summary": "...",
      "key_points": ["...", "..."],
      "insights": ["...", "..."],
      "applications": ["...", "..."]
    }}

    Content:
    {content[:12000]}

    Extra Instructions:
    {extra_prompt}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


def parse_response(text):
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        clean_json = text[start:end]
        return json.loads(clean_json)
    except:
        return {
            "summary": text,
            "key_points": [],
            "insights": [],
            "applications": []
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    link = request.form['youtube_link']
    extra = request.form.get('additional_prompt', "")

    video_id = extract_video_id(link)
    transcript = get_transcript(video_id) if video_id else None

    content = transcript if transcript else link

    raw = generate_summary(content, extra)
    data = parse_response(raw)

    return render_template("result.html", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)