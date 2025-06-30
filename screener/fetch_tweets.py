from screener.config import WATCHLIST, TWEETS_PER_ASSET
import requests, dotenv, os

dotenv.load_dotenv()

url = "https://api.twitterapi.io/twitter/tweet/advanced_search"
headers = {"X-API-Key": os.getenv("api_key")}


def fetch_recent_tweets():
    tweets_by_asset = {}
    for asset in WATCHLIST:
        query = asset
        tweets = []
        querystring = {"queryType":"Latest", "query":query}
        response = requests.request("GET", url, headers=headers, params=querystring)
        twts = response.json()['tweets']
        for tweet in twts:
            tweets.append(tweet["text"])
        tweets_by_asset[asset] = tweets
    return tweets_by_asset