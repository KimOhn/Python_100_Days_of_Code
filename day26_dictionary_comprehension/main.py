import pandas

df= pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:

words = {
    row.letter:row.code for index,row in df.iterrows()
}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def NATO():
    try:
        name = input("What's your name").upper()
        name_words = [words[letter] for letter in name]
    except KeyError:
        print("sorry")
        NATO()
    else:
        print(name_words)

NATO()