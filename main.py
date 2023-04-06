import open_file as text
from processing import stopword_removal, stemming, tokenize, case_folding, normalization
from assets import dictonary
from colorama import Fore, Style
from representing import ohe_bow, bow_tfidf
import os

listOfText = text.of() # Parsing Process
document_normalized = []
for sentence in listOfText:
    os.system('cls')
    print(Fore.RED, "Kalimat awal :", sentence, Style.RESET_ALL)

    print(Fore.CYAN, "Hasil Case Folding:", Style.RESET_ALL)
    caseFolding = case_folding.cf(sentence) # Case Folding Process
    print(caseFolding)

    normalized = normalization.nz(caseFolding, dictonary.dic())
    print(Fore.CYAN, "Hasil Normalisasi:", Style.RESET_ALL) # Normalization Process
    print(normalized)
    document_normalized.append(normalized)

    print(Fore.CYAN, "Hasil Tokenisasi:", Style.RESET_ALL)
    tokenized = tokenize.token(normalized) # Tokenizing Process
    print(tokenized)

    print(Fore.CYAN, "Hasil Filtering:", Style.RESET_ALL)
    filtered = stopword_removal.swr(tokenized) # Stopword Removal/Filtering Process
    print(filtered)

    print(Fore.CYAN, "Hasil Stemming:", Style.RESET_ALL)
    stemmed = stemming.stm(filtered) # Stemming Process
    print(stemmed)

    result = ' '.join(stemmed)
    print(Fore.GREEN, "Kalimat akhir : ", result, Style.RESET_ALL)
    input("Tekan enter untuk melanjutkan")

print(Fore.CYAN, "Representasi One Hot Encoding:", Style.RESET_ALL)
ohe_bow.representing(document_normalized, True)
input("Tekan enter untuk melanjutkan")
print(Fore.CYAN, "Representasi Bag-of-Words:", Style.RESET_ALL)
ohe_bow.representing(document_normalized, False)
input("Tekan enter untuk melanjutkan")
print(Fore.CYAN, "Representasi Bag-of-Words (TFIDF):", Style.RESET_ALL)
bow_tfidf.representing(document_normalized)