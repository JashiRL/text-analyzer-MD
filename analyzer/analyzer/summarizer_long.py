# analyzer/summarizer_long.py

"""
Resumen generativo para textos largos utilizando transformers.
"""

from transformers import pipeline

# Inicializa el pipeline una sola vez
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=250, min_length=100):
    """
    Resume textos largos usando un modelo generativo.
    """
    if not text or not isinstance(text, str):
        return "Texto no válido para resumir."

    try:
        # Limitamos la longitud del texto que se le pasa al modelo
        # El modelo no admite entradas infinitamente largas
        inputs = text[:1024]  # Ajusta según capacidad del modelo/tokenizador

        summary = summarizer(inputs, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error durante el resumen largo: {str(e)}"
