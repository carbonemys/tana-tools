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
    elif (youtube_detail == 'channel'):
        channel_element = soup.find('span', {'itemprop': 'author'})
        if (channel_element):
            channel_name = channel_element.find('link', {'itemprop': 'name'})['content']
            return channel_name
        else:
            return 'Error: channel not found'
    else:
        return 'Error: no detail specified'