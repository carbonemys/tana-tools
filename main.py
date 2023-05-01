import os
from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_from_directory('pages', 'index.html')

@app.route('/youtube_transcript')
def new_endpoint():
    youtube_url = request.args.get('youtube_url')
    from tools.youtube_transcript import youtube_transcript
    return youtube_transcript(youtube_url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))