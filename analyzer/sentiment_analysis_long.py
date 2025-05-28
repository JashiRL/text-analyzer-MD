"""
Análisis de sentimientos para textos largos usando un modelo de emociones en inglés.
"""

from transformers import pipeline

# Se utiliza un modelo multiclase de emociones en inglés
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True,
    top_k=None  # en lugar de usar return_all_scores (ya deprecated)
)

def analyze_sentiment(text):
    """
    Realiza análisis de emociones para textos largos.
    Devuelve un resumen con porcentaje por emoción.
    """
    if not text.strip():
        return {"error": "Texto vacío."}

    try:
        # Limita el texto a 512 tokens por entrada
        results = classifier(text[:512])

        if isinstance(results, list) and isinstance(results[0], list):
            emotion_scores = results[0]
            summary = {e["label"]: round(e["score"] * 100, 2) for e in emotion_scores}
            return {
                "method": "long",
                "summary": summary
            }
        else:
            return {"error": "Error inesperado en el análisis de emociones."}
    except Exception as e:
        return {"error": f"Error al procesar análisis largo: {str(e)}"}
