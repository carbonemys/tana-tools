from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from utils.extract_youtube_id import extract_youtube_id

def youtube_transcript(youtube_url, newline=False):
    youtube_id = extract_youtube_id(youtube_url)
    transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
    formatter = TextFormatter()
    raw_text = formatter.format_transcript(transcript)
    
    if not newline:
        raw_text = raw_text.replace('\n', ' ')

    return raw_text