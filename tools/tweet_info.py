import snscrape.modules.twitter as sntwitter
import json
from urllib.parse import urlparse

def tweet_info(tweet_url):
    path = urlparse(tweet_url).path
    tweet_id = path.split('/')[-1]

    tweet = next(sntwitter.TwitterTweetScraper(str(tweet_id), 
        mode=sntwitter.TwitterTweetScraperMode.SINGLE).get_items())
    tweet_data = json.loads(tweet.json())
    username = tweet_data['user']['username']
    content = tweet_data['renderedContent']
    return username, content