import nltk
from nltk.corpus import stopwords

def swr(tokenized):

    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [token for token in tokenized if token not in stop_words]
    return filtered_tokens