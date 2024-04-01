import sys

def even_or_odd():
    try:
        if  len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
        elif len(sys.argv) == 2:
            nbr = int(sys.argv[1])
            if nbr % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 0

even_or_odd()