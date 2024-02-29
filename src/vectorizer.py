from sklearn.feature_extraction.text import CountVectorizer

class TextVectorizer:
    def __init__(self, stop_words=None, lowercase=True, max_df=1.0, min_df=1, max_features=None, vocabulary=None):
        self.vectorizer = CountVectorizer(stop_words=stop_words, lowercase=lowercase, max_df=max_df, min_df=min_df, max_features=max_features, vocabulary=vocabulary)

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)
