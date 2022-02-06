from asyncio.windows_events import NULL
import collections
from email.policy import strict
from json.encoder import INFINITY
from typing import List


def compute_the_nth_root(radicand, n):
    return radicand ** (1/n)


def get_ordinal_suffix(value) -> str:
    string = str(value)
    if (string.endswith("11")):
        return "th"
    elif (string.endswith("12")):
        return "th"
    elif (string.endswith("13")):
        return "th"
    elif (string.endswith("1")):
        return "st"
    elif (string.endswith("2")):
        return "nd"
    elif (string.endswith("3")):
        return "rd"

    return "th"


def build_ordinal_form(value) -> str:
    return str(value) + get_ordinal_suffix(value)


def display_nth_root(radicand, n) -> str:
    root = compute_the_nth_root(radicand, n)
    message = f"""
        The {build_ordinal_form(n)} root
        of {str(radicand)} is {str(root)}"""
    print(message)

# display_nth_root(16, 4)


def display_all_the_arguments_passed(*args):
    for arg in args:
        print(arg, end=" ")

# display_all_the_arguments_passed("This", "parameter", "list", "is", "variable")


def do_range_addition(value):
    if (value != 0):
        return value + do_range_addition(value - 1)

    return 0

# print(do_range_addition(10))


def find_largest_item(list: List):
    largest = 0
    for item in list:
        if (item > largest):
            largest = item

    return largest

collection = [19, 21, 50, 24, 69, 42]
# print(find_largest_item(collection))


def find_odd_numbers_within_range(start: int, end: int) -> List:
    counter = start
    oddList = []
    while (counter <= end):
        if (counter % 2 != 0):
            oddList.append(counter)
        counter += 1

    return oddList

print(find_odd_numbers_within_range(4, 30))