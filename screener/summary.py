import os
import google.generativeai as genai

# Auto-loads from env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose a lightweight, cost-effective model
MODEL = "gemini-2.5-flash"

def summarize_tweets(asset, tweets):
    prompt = (
        f"Summarize the sentiment about {asset} in these tweets:\n\n"
        + "\n".join(tweets)
        + "\n\nProvide a 1-2 sentence summary focusing on overall sentiment and key themes."
    )
    response = genai.GenerativeModel(MODEL).generate_content(prompt)
    return response.text.strip()
