from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import traceback

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # rather than enabling routes see handle it and should work for securing from Cross-Site Request Forgery (CSRF)

import os
SUMMARIZATION_SERVICE_URL = os.environ.get("SUMMARIZATION_SERVICE_URL", "http://summarization_service:5001/summarize")
@app.route('/', methods=['GET'])
def home():
    return '''
        <h2>Welcome to the YouTube Summarizer API 🚀</h2>
        <p>Use the <code>/summarize</code> endpoint with a POST request to summarize a YouTube video.</p>
        <p>Example POST JSON:</p>
        <pre>{
    "videoLink": "https://www.youtube.com/watch?v=example"
}</pre>
    '''


@app.route('/summarize', methods=['POST'])
def summarize_video():
    try:
        data = request.get_json()
        video_link = data.get("videoLink")

        if not video_link:
            return jsonify({"error": "No video link provided"}), 400

        response = requests.post(SUMMARIZATION_SERVICE_URL, json={"videoLink": video_link})
        response.raise_for_status()

        return jsonify(response.json()), response.status_code
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
