import sys

def valid_args(estr):
    """Check if a string contains both spaces and alphanumeric characters"""
    contains_space = False
    contains_alphanumeric = False
    
    for i in estr:
        if i.isspace():
            contains_space = True
        elif i.isalnum():
            contains_alphanumeric = True
        else:
            return False
            
    return contains_space or contains_alphanumeric

def convert_to_morse(estr):
    """Convert a string to Morse code"""
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "}
    morse_code = ""
    for char in estr:
        if char.upper() in NESTED_MORSE:
            morse_code += NESTED_MORSE[char.upper()]
    return morse_code

def main():
    """do the work f1 + f2"""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    elif not valid_args(sys.argv[1]):
        print("AssertionError: the arguments are bad")
    else:
        morse_code = convert_to_morse(sys.argv[1])
        print(morse_code)

if __name__ == "__main__":
    main()

