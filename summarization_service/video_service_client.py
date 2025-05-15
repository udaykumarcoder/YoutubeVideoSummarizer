import requests
import traceback

def extract_video_id(video_link):
    try:
        response = requests.post("http://video_service:5002/extract_video_id", json={"videoLink": video_link})
        response.raise_for_status()
        return response.json()["videoId"]
    except Exception as e:
        print(traceback.format_exc())
        raise

def get_transcript(video_id, video_link):
    try:
        response = requests.post("http://video_service:5002/get_transcript", json={"videoId": video_id, "videoLink": video_link})
        response.raise_for_status()
        return response.json()["transcript"]
    except Exception as e:
        print(traceback.format_exc())
        raise
