import open_file as text
from processing import stopword_removal, stemming, tokenize, case_folding, normalization
from assets import dictonary
from colorama import Fore, Style
from representing import one_hot_encoding
import os

listOfText = text.of()
document_normalized = []
for sentence in listOfText:
    os.system('cls')
    print(Fore.RED, "Kalimat awal :", sentence, Style.RESET_ALL)

    # Case Folding Process
    print(Fore.CYAN, "Hasil Case Folding:", Style.RESET_ALL)
    caseFolding = case_folding.cf(sentence)
    print(caseFolding)

    # Normalization Process
    normalized = normalization.nz(caseFolding, dictonary.dic())
    print(Fore.CYAN, "Hasil Normalisasi:", Style.RESET_ALL)
    print(normalized)
    document_normalized.append(normalized)

    # Tokenizing Process
    print(Fore.CYAN, "Hasil Tokenisasi:", Style.RESET_ALL)
    tokenized = tokenize.token(normalized)
    print(tokenized)

    # Stopword Removal/Filtering Process
    print(Fore.CYAN, "Hasil Filtering:", Style.RESET_ALL)
    filtered = stopword_removal.swr(tokenized)
    print(filtered)

    # Stemming Process
    print(Fore.CYAN, "Hasil Stemming:", Style.RESET_ALL)
    stemmed = stemming.stm(filtered)
    print(stemmed)
    result = ' '.join(stemmed)
    print(Fore.GREEN, "Kalimat akhir : ", result, Style.RESET_ALL)
    input("Tekan enter untuk melanjutkan")

print("Representasi One Hot Encoding:")
one_hot_encoding.ohe(document_normalized)