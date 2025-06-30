# Mini AI Screener (Crypto/FX Sentiment)

A Python CLI tool that screens sentiment for crypto and forex assets daily using scraped tweets.

## How to Run

```bash
pip install -r requirements.txt
python cli.py
```

Outputs a JSON sentiment report in `output/daily_report.json`

## Assets Tracked
- BTC, ETH, SOL, DOGE
- XAUUSD, EURUSD, GBPUSD, USDJPY

## Output Example
```json
{
  "BTC": {
    "score": 0.71,
    "trend": "Bullish",
    "top_keywords": ["moon", "ETF", "bull", "pump", "$BTC"]
  },
  ...
}
```

## Features
- Fetches recent tweets for selected crypto and forex assets
- Performs sentiment analysis using VADER
- Generates daily sentiment reports in JSON format

## Configuration
Create a `.env` file with your API key:
```
api_key=YOUR_API_KEY_HERE
```

## Requirements
- Python 3.11+
- See [requirements.txt](requirements.txt) for dependencies

## License
MIT License. See [License](License).

## Contributing
Pull requests and issues are welcome!