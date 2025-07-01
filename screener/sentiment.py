from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def analyze_sentiment(tweets_by_asset):
    sia = SentimentIntensityAnalyzer()
    scores = {}
    for asset, tweets in tweets_by_asset.items():
        total_score = 0
        keywords = []
        for tweet in tweets:
            sentiment = sia.polarity_scores(tweet)
            total_score += sentiment['compound']
            keywords.extend([word for word in tweet.split() if word.startswith("$") or word.isalpha()])

        avg_score = total_score / len(tweets) if tweets else 0
        trend = "Bullish" if avg_score > 0.2 else "Bearish" if avg_score < -0.2 else "Neutral"
        scores[asset] = {
            "score": round(avg_score, 3),
            "trend": trend,
            "top_keywords": keywords[:5]
        }
    return scores