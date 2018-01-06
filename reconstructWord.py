
import numpy as np
import re
"""
On reçoit une liste d'array
Chaque array possède la probabilité d'une lettre de l'alphabet (26 cases)
"""
def wordConstruction(letterProbability):
    firstWordTry = dummyWordConstruction(letterProbability)
    if(checkIfDummyWordIsValid(firstWordTry)):
        writtingWordInFiles(firstWordTry)
    else :
        cleverWordConstruction(letterProbability)

def writtingWordInFiles(wordToAdd):
    with open("result.txt","a") as resultText :
        resultText.add(wordToAdd)

    resultText.close()

"""Méthode Dummy"""

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


#On essaye une méthode qui consiste simplement a prendre la lettre la plus probable pour chaque lettres

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

"""
Vérification plus poussé
A partir du dictionnaire l'objectif est de construire pour chaque lettre la probabilité d'être suivi par une autre lettre
Lors de la reconstruction du mot si la probabilité la plus élèvé est inférieur a un seuil donnée
    On compare alors les deux lettre les plus probable avec leur chance d'apparaitre
    On garde alors le meilleursrésultat(par exemple multiplication des proba du réseau et celle obtenu sur le dictionnaire)
"""

def cleverWordConstruction(letterProbability):
    filepathDictionnary = "words_alpha.txt"
    #Valeur de seuil. Si proba en sortie du réseau de neuronne supérieur à cette valeur aucune vérification n'est faite
    #Si la proba est inférieur alors on test avec la seconde lettres
    SAFETY_VALUE = 0.7

    #Variable contenant le tableau des probabilité des lettre en fonction du dictionnaire
    count = constructStatFromDictionnary(filepathDictionnary)

    returnWord = ""
    firstLetter = True
    for letterArray in letterProbability :
        #Pour la première lettre on prend toujours la plus haute valeur disponible
        if firstLetter :
            max = 0
            maxIndex = 0
            for i in range(0, 25):
                if letterArray[i] > max:
                    max = letterArray[i]
                    maxIndex = i

            returnWord += addLetterToWord(maxIndex)

            firstLetter = False

        else :
            max = 0
            maxIndex = 0
            secondMax = 0
            secondMaxIndex = 0

            for i in range(0,25):
                if letterArray[i] > max :
                    secondMax = max
                    secondMaxIndex = maxIndex
                    max = letterArray[i]
                    maxIndex = i

            if max > SAFETY_VALUE :
                returnWord+= addLetterToWord(maxIndex)
            else :
                lastLetterIndex = ord(returnWord[-1:])-96
                maxTest = max * count[lastLetterIndex-1,maxIndex]
                secondMaxTest = secondMax * count[lastLetterIndex-1, secondMaxIndex]

                if maxTest >= secondMaxTest :
                    returnWord+=addLetterToWord(maxIndex)
                else :
                    returnWord+=addLetterToWord(secondMaxIndex)

    writtingWordInFiles(returnWord)

def constructStatFromDictionnary(filepath):
    count = np.zeros(26,26)

    with open(filepath,"r") as lines:
        for line in lines:
            #Pour chaque mot, a partir de la seconde lettre, regarder la lettre qui précède et ajouter dans count a la bonne case +1
            line = line.replace("\n","")
            line2 = list(line)
            for i in range(1,len(line)):
                firstLetter = ord(line2[i-1])-96 #-96 car en python ord('a') = 97
                secondLetter = ord (line2[i])-96
                #Une fois que les deux lettre sont identifié on incrémente de 1 dans la ligne de la première lettre
                #colonne de la seconde lettre

                count[firstLetter-1,secondLetter-1]+=1

    #Pour être rigoureux il faudrait pour chaque ligne faire la somme des résultat obtenu et diviser chaque case par la valeur
    #Mais pour l'utilisation que l'on veut faire par la suite ce n'est pas forcément nécessaire
    lines.close()
    return count

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