# analyzer/sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        emotion = "joy"
    elif polarity < -0.1:
        emotion = "sadness"
    else:
        emotion = "neutral"

    return {
        "method": "short",
        "emotion": emotion,
        "score": round(polarity * 100, 2)
    }
