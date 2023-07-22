import os
from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_from_directory('pages', 'index.html')

@app.route('/youtube_transcript')
def youtube_transcript_endpoint():
    youtube_url = request.args.get('youtube_url')
    newline = request.args.get('newline')

    if newline is not None:
        newline = newline.lower() == 'true'
    else:
        newline = False
        
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

@app.route('/tweet')
def tweet_endpoint():
    tweet_url = request.args.get('tweet_url')
    twitter_detail = request.args.get('twitter_detail', 'content')
    from tools.tweet_info import tweet_info
    username, content = tweet_info(tweet_url)
    if twitter_detail == 'username':
        return username
    else:
        return content

@app.route('/mermaid_graph')
def base64_encode():
    encoded_graph = request.args.get('encoded_graph')
    import base64
    import urllib.parse
    decoded_string = urllib.parse.unquote(encoded_graph)
    graphbytes = decoded_string.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    print("https://mermaid.ink/img/" + base64_string)
    return "https://mermaid.ink/img/" + base64_string

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))