from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

def extract_main_topic(text):
    # Usar stopwords en español
    stop_words = stopwords.words('spanish')
    # stop_words = stopwords.words('english')

    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_sorting = X.toarray().flatten().argsort()[::-1]
    top_words = [feature_array[i] for i in tfidf_sorting[:5]]
    return ', '.join(top_words)
