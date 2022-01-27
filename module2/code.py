import math
import string

def computeFactorial(value: int):
    result = math.factorial(value)
    print('The factorial of', value, 'is', result)

# computeFactorial(10)


def previousAndCurrentRangeSum(rangeSize: int):
    previousNumber: int = 0
    sum: int = 0
    for i in range(rangeSize):
        if (i > 0):
           print('Previous Number:', previousNumber)
           print('Current Number:', i)
           sum = previousNumber + i
           print('Sum', sum)
           previousNumber = i

# previousAndCurrentRangeSum(10)


def printEvenIndexCharacters(word: string):
    print('The characters below are found in odd indexes of the word:', word)
    wordLength = len(word)
    i = 0
    while (i < wordLength):
        if (i % 2 != 0):
            print(word[i])
        i += 1

# printEvenIndexCharacters('television')


def removeFirstNCharacters(word: string, charsToRemove: int):
    wordLength = len(word)
    result = word[charsToRemove:wordLength]
    print(result)

removeFirstNCharacters('Radiohead', 5)