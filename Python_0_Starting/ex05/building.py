import  sys
import string

def letter_punctuation(estr):
    count = 0
    for i in estr:
        if i in string.punctuation:
            count += 1
    return count

def letter_digit(estr):
    count = 0
    for i in estr:
        if i.isdigit():
            count += 1
    return count

def letter_space(estr):
    count = 0
    for i in estr:
        if i.isspace():
            count += 1
    return count

def letter_min(estr):
    count = 0
    for i in estr:
        if i.islower():
            count += 1
    return count

def letter_maj(estr):
    count = 0
    for i in estr:
        if i.isupper():
            count += 1
    return count

def nbr_letter(estr):
    return len(estr)

def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 2:
        print("")
        ok = str(sys.argv[1])
        print(f"The text contains {nbr_letter(ok)} characters:")
        print(f"{letter_maj(ok)} upper letters")
        print(f"{letter_min(ok)} lower letters")
        print(f"{letter_punctuation(ok)} punctuation marks")
        print(f"{letter_space(ok)} spaces")
        print(f"{(letter_digit(ok))} digits")

    elif len(sys.argv) == 1:
        ok = input("What is the text to count?")
        print(f"The text contains {nbr_letter(ok)} characters:")
        print(f"{letter_maj(ok)} upper letters")
        print(f"{letter_min(ok)} lower letters")
        print(f"{letter_punctuation(ok)} punctuation marks")
        print(f"{letter_space(ok)} spaces")
        print(f"{(letter_digit(ok))} digits")
    else:
        print("")


if __name__ == "__main__":
    main()