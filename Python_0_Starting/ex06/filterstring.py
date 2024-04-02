import sys
import re

def main():
    """Check if the conditions are valid for the exercice and do the exercice"""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
    else:
        string_arg = sys.argv[1]
        nbr_arg = sys.argv[2]
        
        if not isinstance(string_arg, str) or not isinstance(nbr_arg, str):
            print("AssertionError: the arguments are bad")
        elif re.search(r'[^A-Za-z0-9\s]', string_arg):
            print("AssertionError: the string contains special characters")
        else:
            try:
                nbr_arg = int(nbr_arg)
            except ValueError:
                print("AssertionError: the arguments are bad")
                return

            words = string_arg.split()
            filtered_words = list(filter(lambda word: len(word) > nbr_arg, words))
            print(filtered_words)

if __name__ == "__main__":
    main()
