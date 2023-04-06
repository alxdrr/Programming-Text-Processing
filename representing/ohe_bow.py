from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def representing(documents, bin):
    # Membuat objek CountVectorizer dengan ketentuan binary = true yang akan menghasilkan representasi biner dari dokumen, di mana nilai 1 hanya diberikan pada kata yang muncul lebih dari 1 kali, sedangkan nilai 0 diberikan pada kata yang muncul sekali atau tidak sama sekali.
    vectorizer = CountVectorizer(binary=bin)

    # Melakukan fit transform pada data
    one_hot = vectorizer.fit_transform(documents)

    # Membuat DataFrame dari hasil Text Representation
    df = pd.DataFrame(one_hot.toarray().transpose(), index=vectorizer.get_feature_names_out(), columns=['Dokumen'+str(i+1) for i in range(len(documents))])
    pd.set_option('display.max_rows', None) #Menampilkan keseluruhan tabel
    # Mencetak hasil One Hot Encoding
    print(df)