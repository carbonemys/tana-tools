import requests
from bs4 import BeautifulSoup

def youtube_detail(youtube_url, youtube_detail):
    response = requests.get(youtube_url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.find('title')

    if (youtube_detail == 'title'):
        video_title = title_element.text.strip()
        video_title = video_title.replace(' - YouTube', '')
        return video_title
    else:
        return 'Error: no detail specified'