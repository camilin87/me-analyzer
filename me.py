from sys import argv
from sys import exit

def main(args):

    if not len(args) >= 2:
        print "ERROR: Missing file to analyze"
        exit()

    filename = args[1]

    print "Analyzing", filename

    with open(filename) as f:
        words = [w.lower() for w in f.read().split(" ")]

        print "Found", len(words), "words"

        for target_word in ["I", "me", "my", "mine", "I'm"]:
            occurrences = len([w for w in words if w == target_word.lower()])
            print "Found", occurrences, "occurrences of", target_word 

if __name__ == "__main__":
    main(argv)
