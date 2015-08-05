from sys import argv
from sys import exit

def main(args):

    if not len(args) >= 2:
        print "ERROR: Missing file to analyze"
        exit()

    print "Analyzing", args[1]

if __name__ == "__main__":
    main(argv)
