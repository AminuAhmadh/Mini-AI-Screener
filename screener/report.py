import json
from datetime import datetime


def generate_daily_report(sentiment_scores):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filepath = f"output/daily_report.json"
    with open(filepath, 'w') as f:
        json.dump({"date": date_str, "data": sentiment_scores}, f, indent=2)
