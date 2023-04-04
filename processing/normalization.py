import re
import string
def nz(sentence, dictonary):
    removed_number = re.sub(r"\d+", "", sentence)
    removed_punctuation = ""
    for char in removed_number:
        if char not in string.punctuation:
            removed_punctuation += char

    word = removed_punctuation.split()
    removed_punctuation = ""
    for i in range(len(word)):
        if word[i] in dictonary:
            word[i] = dictonary[word[i]]
        removed_punctuation += word[i] + ' '

    return removed_punctuation.rstrip()