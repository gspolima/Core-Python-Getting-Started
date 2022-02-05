from email.policy import strict


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

display_nth_root(16, 4)