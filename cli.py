import click
from screener.fetch_tweets import fetch_recent_tweets
from screener.sentiment import analyze_sentiment
from screener.report import generate_daily_report

@click.command()
def run():
    """Run the daily Mini AI Screener."""
    print("🔍 Fetching tweets...")
    tweets = fetch_recent_tweets()

    print("🧠 Analyzing sentiment...")
    sentiment_scores = analyze_sentiment(tweets)

    print("📊 Generating report...")
    generate_daily_report(sentiment_scores, tweets)

    print("✅ Done. Report saved in output/daily_report.json")

if __name__ == '__main__':
    run()