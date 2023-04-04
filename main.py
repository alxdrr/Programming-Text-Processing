import open_file as text
import tokenize as token
import stopword_removal as swr
import stemming as stm
import dictonary as dct
from colorama import Fore, Style
import os

listOfText = text.open_file()


for sentence in listOfText:
    os.system('cls')
    # Tokenizing Process
    print(Fore.RED, "Kalimat awal :", sentence, Style.RESET_ALL)
    print(Fore.CYAN, "Hasil Tokenisasi:", Style.RESET_ALL)
    tokenized = token.tokenize(sentence.lower())
    print(tokenized)
    # Stopword Removal/Filtering Process
    print(Fore.CYAN, "Hasil Filtering:", Style.RESET_ALL)
    filtered = swr.stopword_removal(tokenized)
    print(filtered)
    # Stemming Process
    print(Fore.CYAN, "Hasil Stemming:", Style.RESET_ALL)
    stemmed = stm.stemming(filtered, dct.dic())
    print(stemmed)
    result = ' '.join(stemmed)
    print(Fore.GREEN, "Kalimat akhir : ", result, Style.RESET_ALL)
    input("Tekan enter untuk melanjutkan")
