# analyzer/smart_analyzer.py

"""
Análisis inteligente que selecciona automáticamente la herramienta adecuada según la longitud del texto.
"""

from . import sentiment_analysis
from . import sentiment_analysis_long
from . import summarizer


def analyze_sentiment_smart(text):
    if len(text.split()) < 300:
        print("Usando análisis corto")
        result = sentiment_analysis.analyze_sentiment(text)
    else:
        print("Usando análisis largo")
        result = sentiment_analysis_long.analyze_sentiment(text)

    print("Resultado crudo:", result) 

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
        return {"error": "Formato de salida inesperado."}

def summarize_text_smart(text):
    """
    Usa la función adecuada para resumir el texto según su longitud.
    """
    try:
        if len(text.split()) < 300:
            return summarizer.summarize_with_sumy(text)
        else:
            
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
