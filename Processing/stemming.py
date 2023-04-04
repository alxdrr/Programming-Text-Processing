# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
def stm(filtering):
    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    for i in range(len(filtering)):
        filtering[i] = stemmer.stem(filtering[i])

    stemmed = filtering
    return stemmed