from typing import List, Tuple


def split_string_by_separator(string: str, separator: str):
    splitted = string.split(separator)
    joined = ' '.join(splitted)
    return joined

# print(split_string_by_separator('Emma-is-a-data-scientist','-'))


def turn_tuple_into_string(tuple: Tuple):
    result = ' '.join(tuple)
    return result

# print(turn_tuple_into_string(('This', 'is', 'a', 'tuple')))


def replace_4th_and_4th_to_last_element(list: List):
    if (list.__len__() < 7):
        return None

    if (list[-4] != 42):
        list[-4] = 42

    if (list[3] != 68):
        list[3] = 68

    return list

print(replace_4th_and_4th_to_last_element([1, 3, 12, 40, 94, 97, 91, 89]))