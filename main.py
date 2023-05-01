import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route('/youtube_transcript')
def new_endpoint():
    youtube_url = request.args.get('youtube_url')
    from tools.youtube_transcript import youtube_transcript
    return youtube_transcript(youtube_url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))