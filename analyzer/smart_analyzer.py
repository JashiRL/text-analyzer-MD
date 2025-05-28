# analyzer/smart_analyzer.py

"""
Análisis inteligente que selecciona automáticamente la herramienta adecuada según la longitud del texto.
"""

from . import sentiment_analysis
from . import sentiment_analysis_long
from . import summarizer
# summarizer_long es opcional y aún puede no estar implementado

def analyze_sentiment_smart(text):
    """
    Usa el módulo adecuado según la longitud del texto para análisis de emociones.
    """
    try:
        if len(text.split()) < 300:
            result = sentiment_analysis.analyze_sentiment(text)
        else:
            result = sentiment_analysis_long.analyze_sentiment(text)

        if "summary" in result:
            return {
                "method": result.get("method", "smart"),
                "summary": result["summary"]
            }
        elif "emotion" in result:
            return {
                "method": result.get("method", "smart"),
                "emotion": result["emotion"],
                "confidence": result.get("confidence", result.get("score", 0))
            }
        else:
            return {"error": "Formato de salida inesperado del análisis de sentimiento."}
    except Exception as e:
        return {"error": f"Error durante análisis de sentimientos: {str(e)}"}

def summarize_text_smart(text):
    """
    Usa la función adecuada para resumir el texto según su longitud.
    """
    try:
        if len(text.split()) < 300:
            return summarizer.summarize_with_sumy(text)
        else:
            # Usa summarizer_long si está disponible
            try:
                from . import summarizer_long
                if hasattr(summarizer_long, "summarize_text"):
                    return summarizer_long.summarize_text(text)
                else:
                    return "La función summarize_text no está implementada en summarizer_long."
            except ImportError:
                return "Resumen largo no disponible. Asegúrate de que summarizer_long.py exista."
    except Exception as e:
        return f"Error durante el resumen: {str(e)}"
