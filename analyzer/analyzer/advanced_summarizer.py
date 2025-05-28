from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Puedes cambiar "spanish" por "english" según el idioma del texto.
DEFAULT_LANGUAGE = "spanish"

def summarize_with_sumy(text, num_sentences=5, language=DEFAULT_LANGUAGE):
    """
    Resume el texto usando el algoritmo extractivo LexRank (sumy).
    """
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)


# === OPCIONAL: Plantilla para integrar un modelo generativo (transformers) ===
# Para usarlo necesitarás instalar e importar HuggingFace (transformers)
# y descargar un modelo como `facebook/bart-large-cnn` o `t5-base`.

"""
from transformers import pipeline

# Inicializar fuera de la función si deseas usarlo varias veces
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_with_transformer(text, max_length=150, min_length=40):
    summary = summarization_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
"""
