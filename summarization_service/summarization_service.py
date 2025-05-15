from flask import Flask, request, jsonify
import traceback
from summarizer import get_summary

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''
        <h2>Welcome to the  Summarizer Service🚀</h2>
        
    '''


@app.route('/summarize', methods=['POST'])
def summarize_video():
    try:
        data = request.get_json()
        video_link = data.get("videoLink")

        if not video_link:
            return jsonify({"error": "No video link provided"}), 400

        transcript, summary = get_summary(video_link)

        return jsonify({"summary": summary, "transcript": transcript}), 200
    except Exception as e:
        error_message = str(e)
        stack_trace = traceback.format_exc()
        print(f"Error: {error_message}\nStack Trace: {stack_trace}")
        return jsonify({"error": error_message, "stackTrace": stack_trace}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)



# from flask import Flask, request, jsonify
# import traceback
# import os

# app = Flask(__name__)

# @app.route('/summarize', methods=['POST'])
# def summarize_video():
#     try:
#         # from summarizer import get_summary  # <- moved here
#         data = request.get_json()
#         video_link = data.get("videoLink")

#         if not video_link:
#             return jsonify({"error": "No video link provided"}), 400

#         transcript, summary = get_summary(video_link)

#         return jsonify({"summary": summary, "transcript": transcript}), 200
#     except Exception as e:
#         error_message = str(e)
#         stack_trace = traceback.format_exc()
#         print(f"Error: {error_message}\nStack Trace: {stack_trace}")
#         return jsonify({"error": error_message, "stackTrace": stack_trace}), 500

# @app.route('/', methods=['GET'])
# def list_files():
#     files = os.listdir(".")
#     file_structure = {}
#     for f in files:
#         if os.path.isdir(f):
#             file_structure[f] = os.listdir(f)
#         else:
#             file_structure[f] = "file"
#     return jsonify({"cwd": os.getcwd(), "files": file_structure})

# if __name__ == "__main__":
#     app.run(port=5001, debug=True)
