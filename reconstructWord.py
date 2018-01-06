
"""
On reçoit une liste d'array
Chaque array possède la probabilité d'une lettre de l'alphabet (26 cases)
"""
def wordConstruction(letterProbability):
    firstWordTry = dummyWordConstruction(letterProbability)
    firstWordSize = len(firstWordTry)
    if(checkIfDummyWordIsValid(firstWordTry)):
        writtingWordInFiles(firstWordTry)




def writtingWordInFiles(wordToAdd):
    with open("result.txt","a") as resultText :
        resultText.add(wordToAdd)

    resultText.close()


def checkIfDummyWordIsValid (word):
    dummyPass = False
    with open ("words_alpha","r") as words_Alpha:
        wordsList = words_Alpha.read()
        lignes = wordsList.split("\n")
        for testWord in lignes:
            if testWord == word :
                dummyPass = True
                break

    words_Alpha.close()
    return dummyPass

"""
On essaye une méthode qui consiste simplement a prendre la lettre la plus probable pour chaque lettres
"""
def dummyWordConstruction (letterProbability):
    dummyWord = ""
    for letterArray in letterProbability :
        max = 0
        maxIndex = 0
        for i in range(0,25) :
            if letterArray[i] > max :
                max = letterArray[i]
                maxIndex = i

        dummyWord += addLetterToWord(maxIndex)


    return dummyWord

def addLetterToWord(LetterNumber):
    return{
        "a" : 1,
        "b" : 2,
        "c":  3,
        "d":  4,
        "e":  5,
        "f":  6,
        "g":  7,
        "h":  8,
        "i":  9,
        "j":  10,
        "k":  11,
        "l":  12,
        "m":  13,
        "n":  14,
        "o":  15,
        "p":  16,
        "q":  17,
        "r":  18,
        "s":  19,
        "t":  20,
        "u":  21,
        "v":  22,
        "w":  23,
        "x":  24,
        "y":  25,
        "z":  26,
    }(LetterNumber)