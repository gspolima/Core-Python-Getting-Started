import math
from operator import index
from turtle import st
from urllib.request import urlopen

def combineFirstMiddleAndLastLetters(word: str):
    letterCount = word.__len__()
    middleIndex = math.floor(letterCount / 2)
    middleLetter = word[middleIndex]

    print(word[0], middleLetter, word[letterCount - 1])

# combineFirstMiddleAndLastLetters("Crafstman")


def placeUppercaseLast(word: str):
    uppercaseLetters = []
    for letter in word:
        if (letter.isupper()):
            uppercaseLetters.append(letter)

    for letter in uppercaseLetters:
        word = word.replace(letter, "", 1)
        word = word + letter

    print(word)

# placeUppercaseLast("PyNaTive")


def createMixedString(firstWord: str, secondWord: str):
    indexStart = 0
    secondWordLength = secondWord.__len__()
    indexEnd = secondWordLength
    newString = ""

    while (indexStart < secondWordLength and indexEnd >= 0):
        newString = newString + firstWord[indexStart] + secondWord[indexEnd - 1]
        indexStart += 1
        indexEnd -= 1

    print(newString)

createMixedString("Cake", "Rice")