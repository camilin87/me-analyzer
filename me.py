from sys import argv
from sys import exit
from os.path import expanduser

OFFENDING_WORDS = [
    "I", "me", "my", "mine", "I'm",
    "you", "you're", "your",
    "yours", "our"
]

def _sanitize_word(word):
    CHARACTERS_TO_ESCAPE = ['"', '`']

    word = word.lower()

    for quote_char in CHARACTERS_TO_ESCAPE:
        word = word.replace(quote_char, '')

    return word

def main(args):
    if not len(args) >= 2:
        print "ERROR: Missing file to analyze"
        exit()

    filename = expanduser(args[1])

    print "Analyzing", filename

    with open(filename) as f:
        all_words = f.read().split(" ")
        words = [_sanitize_word(w) for w in all_words]

        print "Found", len(words), "words"
        total_occurrences = 0

        for target_word in OFFENDING_WORDS:
            occurrences = [w for w in words if w == target_word.lower()]
            occurrences_count = len(occurrences)
            total_occurrences += occurrences_count
            print target_word.rjust(10), "=>", occurrences_count, "times"  

        print "Found", total_occurrences, "offending words"

if __name__ == "__main__":
    main(argv)
