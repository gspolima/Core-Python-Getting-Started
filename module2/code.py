import math
import string

def compute_factorial(value: int):
    result = math.factorial(value)
    print('The factorial of', value, 'is', result)

# compute_factorial(10)


def previous_and_current_range_sum(range_size: int):
    previous_number: int = 0
    sum: int = 0
    for i in range(range_size):
        if (i > 0):
           print('Previous Number:', previous_number)
           print('Current Number:', i)
           sum = previous_number + i
           print('Sum', sum)
           previous_number = i

# previous_and_current_range_sum(10)


def print_even_index_characters(word: string):
    print('The characters below are found in odd indexes of the word:', word)
    word_length = len(word)
    i = 0
    while (i < word_length):
        if (i % 2 != 0):
            print(word[i])
        i += 1

# print_even_index_characters('television')


def remove_first_n_characters(word: string, chars_to_remove: int):
    word_length = len(word)
    result = word[chars_to_remove:word_length]
    print(result)

remove_first_n_characters('Radiohead', 5)