import math
from operator import index
from turtle import st
from urllib.request import urlopen

def combine_first_middle_and_last_letters(word: str):
    letter_count = word.__len__()
    middle_index = math.floor(letter_count / 2)
    middle_letter = word[middle_index]

    print(word[0], middle_letter, word[letter_count - 1])

# combine_first_middle_and_last_letters("Crafstman")


def place_uppercase_last(word: str):
    uppercase_letters = []
    for letter in word:
        if (letter.isupper()):
            uppercase_letters.append(letter)

    for letter in uppercase_letters:
        word = word.replace(letter, "", 1)
        word = word + letter

    print(word)

# place_uppercase_last("PyNaTive")


def create_mixed_string(first_word: str, second_word: str):
    index_start = 0
    second_word_length = second_word.__len__()
    index_end = second_word_length
    new_string = ""

    while (index_start < second_word_length and index_end >= 0):
        new_string = new_string + first_word[index_start] + second_word[index_end - 1]
        index_start += 1
        index_end -= 1

    print(new_string)

create_mixed_string("Cake", "Rice")