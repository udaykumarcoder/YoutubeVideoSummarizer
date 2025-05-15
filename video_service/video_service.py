from flask import Flask, request, jsonify
from yt_utils import extract_video_id, get_transcript
import traceback

app = Flask(__name__)

@app.route('/extract_video_id', methods=['POST'])
def extract_video_id_route():
    try:
        data = request.get_json()
        video_link = data.get("videoLink")

        if not video_link:
            return jsonify({"error": "No video link provided"}), 400

        video_id = extract_video_id(video_link)
        return jsonify({"videoId": video_id}), 200
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/get_transcript', methods=['POST'])
def get_transcript_route():
    try:
        data = request.get_json()
        video_id = data.get("videoId")
        video_link = data.get("videoLink")

        if not video_id or not video_link:
            return jsonify({"error": "Missing video ID or link"}), 400

        transcript = get_transcript(video_id, video_link)
        return jsonify({"transcript": transcript}), 200
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002, debug=True)
