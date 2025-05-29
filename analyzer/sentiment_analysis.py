from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    result = classifier(text[:512])[0]  
    label = result["label"]
    score = result["score"]

    return {
        "method": "short",
        "emotion": label,
        "confidence": round(score * 100, 2)
    }
