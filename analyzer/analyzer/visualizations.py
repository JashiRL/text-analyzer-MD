# analyzer/visualizations.py

import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import seaborn as sns
import re

def clean_and_tokenize(text):
    """Tokeniza y limpia el texto en palabras."""
    return re.findall(r'\b\w+\b', text.lower())

def plot_word_frequency(text, top_n=10):
    """Muestra una gráfica de barras con las palabras más frecuentes."""
    words = clean_and_tokenize(text)
    common = Counter(words).most_common(top_n)

    if not common:
        print("No se encontraron palabras.")
        return

    labels, counts = zip(*common)
    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color='orange')
    plt.title('Frecuencia de Palabras (Top {})'.format(top_n))
    plt.xticks(rotation=45)
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

def plot_word_distribution(text, top_n=30):
    """Gráfica de cajas para mostrar la distribución de longitud de palabras frecuentes."""
    words = clean_and_tokenize(text)
    word_lengths = [len(w) for w in words]

    if not word_lengths:
        print("Texto vacío o sin palabras válidas.")
        return

    plt.figure(figsize=(8, 4))
    sns.boxplot(word_lengths, color='lightblue')
    plt.title("Distribución de longitud de palabras")
    plt.xlabel("Número de caracteres")
    plt.tight_layout()
    plt.show()

def generate_wordcloud(text):
    """Genera y muestra una nube de palabras."""
    words = clean_and_tokenize(text)
    word_freq = Counter(words)
    
    if not word_freq:
        print("No hay suficientes palabras para generar una nube.")
        return

    wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Nube de Palabras")
    plt.tight_layout()
    plt.show()

def plot_sentiment_distribution(summary, filename="sentiment_plot.png"):
    """Muestra una gráfica de barras con la distribución de emociones."""
    if not summary:
        print("No se pudo generar la gráfica de emociones: datos vacíos.")
        return

    emotions = list(summary.keys())
    scores = list(summary.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(emotions, scores, color='skyblue')
    plt.title("Distribución de Emociones")
    plt.xlabel("Emoción")
    plt.ylabel("Porcentaje (%)")

    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{score:.1f}%', ha='center')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
