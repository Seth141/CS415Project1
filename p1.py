import numpy as np


def equal():
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    if num1 == num2:
        print("equal")
        return True
    else:
        print("not equal")


def less():
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    if num1 < num2:
        print("less than")
        return True
    else:
        print("error")


if __name__ == "__main__":
    equal()
    less()
