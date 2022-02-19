def splitStringBySeparator(string: str, separator: str):
    splitted = string.split(separator)
    joined = ' '.join(splitted)
    return joined

result = splitStringBySeparator('Emma-is-a-data-scientist','-')
print(result)