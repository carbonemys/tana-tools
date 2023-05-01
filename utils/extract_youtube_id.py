def extract_youtube_id(url):
    """
    Extracts the YouTube ID from a YouTube URL and returns it.
    If the input is already a valid YouTube ID, returns the input.
    """
    print(url)
    if "youtube.com/watch" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    else:
        return url