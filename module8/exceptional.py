import sys


DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10'
}


def convert(s):
    '''Convert a string to an integer.

        Args:
            s: A sequence of numbers as written

        Returns:
            The integer equivalent of the given sequence
    '''
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]

        print(f'Conversion succeeded!')
        return int(number)

    except (KeyError, TypeError) as exception:
        print(f"Conversion error: {exception!r}",
              file=sys.stderr)
        return -1