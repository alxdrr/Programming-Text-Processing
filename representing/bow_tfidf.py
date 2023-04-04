from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd

# Dokumen yang akan diproses
def representing(documents):

    # Konversi teks menjadi vektor bag-of-words
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)

    # Hitung bobot TFIDF
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)

    # Tampilkan hasil sebagai tabel
    df = pd.DataFrame(tfidf.toarray().transpose(), index=vectorizer.get_feature_names_out(), columns=['Dokumen'+str(i+1) for i in range(len(documents))])
    print(df)