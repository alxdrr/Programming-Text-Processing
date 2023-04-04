# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
def stemming(filtering, dictonary):
    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    for i in range(len(filtering)):
        if filtering[i] in dictonary:
            filtering[i] = dictonary[filtering[i]]
            # print(filtering[i])
        # stemming process
        filtering[i] = stemmer.stem(filtering[i])
        # print(filtering[i])
    stemmed = filtering
    return stemmed