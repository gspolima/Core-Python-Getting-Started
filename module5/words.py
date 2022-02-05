import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words over HTTP from a URL
 
        Args:
            url: a URL from where words will be fetched

        Returns:
            A list of words as strings from 
            the specified document
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)

if (__name__ == "__main__"):
    main(sys.argv[1]) # The first argument ([0]) is the module name
    help(fetch_words)