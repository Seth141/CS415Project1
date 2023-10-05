from math import *


def simplify_fraction(p, q):
    # Calculate the greatest common divisor (GCD) of p and q
    common_divisor = gcd(p, q)

    # Simplify the fraction by dividing both numerator and denominator by the GCD
    simplified_p = p // common_divisor
    simplified_q = q // common_divisor

    return (simplified_p, simplified_q)


def add_fractions(fraction1, fraction2):
    p1, q1 = fraction1
    p2, q2 = fraction2

    # Find a common denominator
    common_denominator = q1 * q2

    # Adjust the numerators to have the common denominator
    adjusted_p1 = p1 * (common_denominator // q1)
    adjusted_p2 = p2 * (common_denominator // q2)

    # Add the numerators
    result_numerator = adjusted_p1 + adjusted_p2

    return simplify_fraction(result_numerator, common_denominator)


def subtract_fractions(fraction1, fraction2):
    p1, q1 = fraction1
    p2, q2 = fraction2

    # Find a common denominator
    common_denominator = q1 * q2

    # Adjust the numerators to have the common denominator
    adjusted_p1 = p1 * (common_denominator // q1)
    adjusted_p2 = p2 * (common_denominator // q2)

    # Subtract the numerators
    result_numerator = adjusted_p1 - adjusted_p2

    return simplify_fraction(result_numerator, common_denominator)


def multiply_fractions(fraction1, fraction2):
    p1, q1 = fraction1
    p2, q2 = fraction2

    # Multiply the numerators and denominators separately
    result_numerator = p1 * p2
    result_denominator = q1 * q2

    return simplify_fraction(result_numerator, result_denominator)


def divide_fractions(fraction1, fraction2):
    p1, q1 = fraction1
    p2, q2 = fraction2

    # To divide fractions, multiply the first fraction by the reciprocal of the second fraction
    reciprocal_fraction2 = (q2, p2)

    return multiply_fractions(fraction1, reciprocal_fraction2)


# checking if the two fractions are equal:
def checkIfEqual(fraction1, fraction2):
    if fraction1 == fraction2:
        # print("The fractions are equal")
        return True
    else:
        # print("The fractions are not equal")
        return False


# checking if the first fraction is less than the second:
def less(fraction1, fraction2):
    if fraction1 < fraction2:
        # print("The first fraction is less than the second")
        return True
    else:
        # print("The first fraction is not less than the second")
        return False


def hSum2(n):
    j = 1
    sum1 = 0
    while sum1 < n:
        sum1 += 1 / j
        j += 1
    return j


def fibonacci(n):
    if n == 0:
        return 1 / 2
    elif n == 1:
        return 1 / 3
    else:
        fib_sequence = [1 / 2, 1 / 3]
        for i in range(2, n + 1):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence[n]
    




    


def main():
    p1 = int(input("Enter the numerator of the first fraction: "))
    q1 = int(input("Enter the denominator of the first fraction: "))
    p2 = int(input("Enter the numerator of the second fraction: "))
    q2 = int(input("Enter the denominator of the second fraction: "))

    while True:
        fraction1 = (p1, q1)
        fraction2 = (p2, q2)

        print("\n")
        print("Menu:")
        print("1. Problem 1a")
        print("2. Problem 1b")
        print("3. Problem 2")
        print("4. Problem 5")
        print("5. Quit")

        print("\n")
        checkIfEqual(fraction1, fraction2)
        less(fraction1, fraction2)

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            print("Enter n: ")
            n = int(input())
            hSum2(n)
            result = hSum2(n)
            print(f"Smallest j:", result)
        elif choice == "2":
            print("Enter n: ")
            n2 = int(input())
            fibonacci(n2)
            result2 = fibonacci(n2)
            print(f"Fibonacci: ", result2)
        elif choice == "3":
            result = multiply_fractions(fraction1, fraction2)
            print(f"The result of multiplication is: {result[0]}/{result[1]}")
        elif choice == "4":
            print("choice under revisions")
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
