from cgi import test
from multiprocessing.dummy import Array
from operator import indexOf


def staircase_pattern(steps: int):    
    for i in range(steps + 1):
        j: int = 1
        while (j <= i):
            print(j, end=" ")
            j += 1

        print("")

# staircase_pattern(5)


def sum_of_all_numbers(limit: int):
    total: int = 0
    while (limit > 0):
        total += limit
        limit -= 1
    print(total)

# sum_of_all_numbers(10)


def multiplication_table_of(number: int):
    multiplier: int = 1;
    while(multiplier <= 10):
        print(number * multiplier)
        multiplier += 1

# multiplication_table_of(4)


def count_digits(number: int):
    number_as_string = str(number)
    digits = len(number_as_string)
    print(digits)

# count_digits(315000000)


def filtered_numbers(array):
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

# filtered_numbers([12, 75, 150, 180, 145, 525, 50])


def fibonacci_sequence(elements_limit: int):
    first = 0
    second = 1
    counter = 2
    print(first, second, end=" ")
    while (counter < elements_limit):
        next = first + second
        print(next, end=" ")
        first = second
        second = next
        counter += 1

# fibonacci_sequence(10)


def count_substring_occurrences(term: str, text: str):
    occurrences = 0
    while (True):
        at_index = text.find(term)
        if (at_index != -1):
            text = text.replace("Emma", "", 1)
            occurrences += 1
        else:
            break

    print("The term", term, "occurs", occurrences, "times")

count_substring_occurrences("Emma", "Emma plays Hide-and-seek. Emma is a writer. Emma eats avocados.")