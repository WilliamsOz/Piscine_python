import sys


def check_odd_or_even(value):
    if value % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    try:
        if len(sys.argv) < 2:
            exit()
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
        exit(1)

    check_odd_or_even(number)

except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
