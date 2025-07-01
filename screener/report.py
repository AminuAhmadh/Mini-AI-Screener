import json
from datetime import datetime
from screener.summary import summarize_tweets



def generate_daily_report(sentiment_scores, tweets_by_asset):
    date_str = datetime.now().strftime("%Y-%m-%d")
    # Add sentiment summary for each asset before writing the file
    for asset, data in sentiment_scores.items():
        tweets = tweets_by_asset.get(asset, [])
        data["summary"] = summarize_tweets(asset, tweets)

    filepath = "output/daily_report.json"
    with open(filepath, 'w') as f:
        json.dump({"date": date_str, "data": sentiment_scores}, f, indent=2)