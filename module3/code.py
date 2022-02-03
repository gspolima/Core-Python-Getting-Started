from cgi import test
from multiprocessing.dummy import Array
from operator import indexOf


def staircasePattern(steps: int):    
    for i in range(steps + 1):
        j: int = 1
        while (j <= i):
            print(j, end=" ")
            j += 1

        print("")

# staircasePattern(5)


def sumOfAllNumbers(limit: int):
    total: int = 0
    while (limit > 0):
        total += limit
        limit -= 1
    print(total)

# sumOfAllNumbers(10)


def multiplicationTableOf(number: int):
    multiplier: int = 1;
    while(multiplier <= 10):
        print(number * multiplier)
        multiplier += 1

# multiplicationTableOf(4)


def countDigits(number: int):
    numberString = str(number)
    digits = len(numberString)
    print(digits)

# countDigits(315000000)


def filteredNumbers(array):
    for i in array:
        if (i % 5 != 0):
            continue
        else:
            if (i > 150):
                continue
            elif (i > 500):
                break
            else:
                print(i)

# filteredNumbers([12, 75, 150, 180, 145, 525, 50])


def fibonacciSequence(limit: int):
    first = 0
    second = 1
    counter = 2
    print(first, second, end=" ")
    while (counter < limit):
        next = first + second
        print(next, end=" ")
        first = second
        second = next
        counter += 1

# fibonacciSequence(10)


def countSubstringOccurrences(term: str, text: str):
    occurrences = 0
    while (True):
        atIndex = text.find(term)
        if (atIndex != -1):
            text = text.replace("Emma", "", 1)
            occurrences += 1
        else:
            break

    print("The term", term, "occurs", occurrences, "times")

countSubstringOccurrences("Emma", "Emma plays Hide-and-seek. Emma is a writer. Emma eats avocados.")