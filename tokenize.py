import string
def tokenize(sentence):
    splitted = sentence.split()
    no_punct = []

    for word in splitted:
        no_punct_word = ""
        for char in word:
            if char not in string.punctuation:
                no_punct_word += char
        no_punct.append(no_punct_word)
        
    return list(filter(bool, no_punct))

