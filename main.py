import os
from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_from_directory('pages', 'index.html')

@app.route('/youtube_transcript')
def youtube_transcript_endpoint():
    youtube_url = request.args.get('youtube_url')
    from tools.youtube_transcript import youtube_transcript
    return youtube_transcript(youtube_url)

@app.route('/youtube_detail')
def youtube_detail_endpoint():
    youtube_url = request.args.get('youtube_url')
    youtube_detail_args = request.args.get('youtube_detail')
    from tools.youtube_detail import youtube_detail
    return youtube_detail(youtube_url, youtube_detail_args)

@app.route('/pdf_transcript')
def pdf_transcript_endpoint():
    pdf_url = request.args.get('pdf_url')
    from tools.pdf_transcript import pdf_transcript
    return pdf_transcript(pdf_url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))