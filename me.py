from sys import argv
from sys import exit

OFFENDING_WORDS = [
    "I", "me", "my", "mine", "I'm",
    "you", "you're", "your"
]

def main(args):

    if not len(args) >= 2:
        print "ERROR: Missing file to analyze"
        exit()

    filename = args[1]

    print "Analyzing", filename

    with open(filename) as f:
        words = [w.lower() for w in f.read().split(" ")]

        print "Found", len(words), "words"

        for target_word in OFFENDING_WORDS:
            occurrences = [w for w in words if w == target_word.lower()]
            print target_word.rjust(10), "=>", len(occurrences), "times"  

if __name__ == "__main__":
    main(argv)
