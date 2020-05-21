import math


def rightangleup(numrows):
    for i in range(1, numrows + 1):
        print("* " * i)


def rightangledown(numrows):
    x = '*'
    for i in range(numrows):
        print('* ' * (numrows - i))


def diamnd(numrows):
    halfrange = math.ceil(numrows / 2)
    for i in range(1,halfrange+1):
        print(" " * (halfrange-i), '* ' * i)
    for i in range(halfrange-1):
        print(" " * (i+1), '* ' * (halfrange-1-i))


def main():
    numrows = int(input("Enter number of rows: "))
    print("\nprinting rignt angled hyportuneus to right up triangle :\n")
    rightangleup(numrows)
    print("\nprinting right angled hypotenuse to right  down triangle :\n")
    rightangledown(numrows)
    print("\nprinting diamond : \n")
    diamnd(numrows)


if __name__ == '__main__':
    main()
