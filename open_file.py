def of():
    with open("assets\Phrase.txt", encoding='latin-1') as file:
        lines = file.readlines()
        sentences = [line.strip() for line in lines]
        return sentences