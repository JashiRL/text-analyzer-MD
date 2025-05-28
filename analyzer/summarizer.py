from . import advanced_summarizer

def summarize_with_sumy(text, num_sentences=5, language="spanish"):
    """
    Función wrapper para resumen extractivo usando sumy desde advanced_summarizer.
    """
    return advanced_summarizer.summarize_with_sumy(text, num_sentences, language)

def summarize_text(text, method="sumy", **kwargs):
    """
    Punto de entrada principal para resumir texto. Permite escoger método.
    Por ahora, solo soporta Sumy.
    """
    if method == "sumy":
        return summarize_with_sumy(text, **kwargs)
    else:
        raise ValueError(f"Método de resumen '{method}' no soportado.")
