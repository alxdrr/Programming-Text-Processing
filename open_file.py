def open_file():
    with open('Phrase.txt', encoding='latin-1') as file:
        lines = file.readlines()
        sentences = [line.strip() for line in lines]
        return sentences