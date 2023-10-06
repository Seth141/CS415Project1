# CS415 Project 1
# Seth N and Adam E

import random
import math
from math import gcd


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


#
#
# Segment 2:
#
#


def primality(N):
    # input: positive int N
    # output: true/false

    # pick a positive int a<N at random
    a = random.randint(1, N)

    if (a ** (N - 1)) % N == (1 % N):
        return True
    else:
        return False


def primality2(N, k):
    for i in range(k):
        result = primality(N)
        if result == False:
            return result

    return result


def primality3(N, k):
    # int N and confidence prarameter k
    # output: true/false

    if N == 2 or N == 3 or N == 5 or N == 7 or N == 11:
        return True
    if N % 2 == 0:
        return False
    if N % 3 == 0:
        return False
    if N % 5 == 0:
        return False
    if N % 7 == 0:
        return False
    if N % 11 == 0:
        return False

    return primality2


def problem2(test1, test2):
    if primality3(test1, test2):
        print("Yes, n is prime.")
    else:
        print("No, n is not prime.")


# problem 3
# Given integers n and k, generate a random prime number P with n bits with a guarantee that P is a prime with probability at least 2**(-k).
# Implement a solution as follows: generate a random n-2 binary string and add 1 as the first and the last bit to create an n bit integer and convert it to decimal.
# (The reason for the first bit to be 1 is that we want the number to be odd. The last bit should be 1 since we want no leading 0's.)
# Then, call primality3 algorithm you in implemented in Problem 2 with n and k as inputs. (k is the second parameter in primality3 which is the number of times the Fermat's test is repeated.)
# Repeat calling primaility3 until it outputs 'yes'. At this point, you have found a prime number (with a probability at least 2**(-k)).


def randomnumber(n):
    # input: n is number of bits in the binary number
    # output: random odd int in decimal
    binarynumber = "1"

    for i in range(n - 2):
        binarynumber = binarynumber + random.choice(["0", "1"])
    binarynumber = binarynumber + "1"

    return int(binarynumber, 2)


def is_prime_double_check(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# problem 4
# Given integers n and k, call the algorithm for Problem 3 (with n and k as inputs) to generate
# two primes p and q with n bits each, and use them to generate the encryption keys E and the
# decryption key D. After computing p and q, compute N = pq. Then, find a random 10 bit
# integer E such that gcd (E, (p - 1)(q - 1)) = 1. Next, find D such that DE = 1 (mod N)
# using extended Euclid's algorithm. Output N, E and D.


def problem4a():
    randomN = int(input("\nProblem 4: input n:"))
    testk = int(input("\nProblem 4: input k:"))

    isprime = False
    while not isprime:
        testN = randomnumber(randomN)
        isprime = primality3(testN, testk)
    p = testN

    isprime = False
    while not isprime:
        testN = randomnumber(randomN)
        isprime = primality3(testN, testk)
    q = testN

    N = p * q
    relativelyprime = False
    while not relativelyprime:
        E = ""
        for i in range(10):
            E = E + random.choice(["0", "1"])
        E = int(E, 2)
        if gcd(E, (p - 1) * (q - 1)) == 1:
            relativelyprime = True

    D = E**-1 % (p - 1) * (q - 1)

    return int(N), int(E), int(D)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def problem4():
    while True:
        p = random.randint(2**10, 2**16)
        if is_prime_double_check(p):
            break
    while True:
        q = random.randint(2**10, 2**16)
        if is_prime_double_check(q) and q != p:
            break

    N = p * q
    phi_N = (p - 1) * (q - 1)

    while True:
        E = random.randint(2, phi_N - 1)
        if gcd(E, phi_N) == 1:
            break

    D = mod_inverse(E, phi_N)

    return N, E, D


def encrypt_and_decrypt_message(N, E, D, message):
    # Encrypt
    encrypted_message = [pow(ord(char), E, N) for char in message]

    # Decrypt
    decrypted_message = "".join([chr(pow(char, D, N)) for char in encrypted_message])

    return encrypted_message, decrypted_message


"""
if __name__ == "__main__":
    problem4a()
    N, E, D = problem4()
    print("RSA Keys Generated:")
    print("N:", N)
    print("E:", E)
    print("D:", D)

    message = input("Enter the plaintext message to encrypt: ")
    encrypted_message, decrypted_message = encrypt_and_decrypt_message(N, E, D, message)

    print("\nEncrypted Message:")
    print(encrypted_message)
    print("\nDecrypted Message:")
    print(decrypted_message)
"""

# Central main:


def main():
    """These are for all fraction operations. Just uncomment to use:"""
    # p1 = int(input("Enter the numerator of the first fraction: "))
    # q1 = int(input("Enter the denominator of the first fraction: "))
    # p2 = int(input("Enter the numerator of the second fraction: "))
    # q2 = int(input("Enter the denominator of the second fraction: "))
    # fraction1 = (p1, q1)
    # fraction2 = (p2, q2)
    # checkIfEqual(fraction1, fraction2)
    # less(fraction1, fraction2)

    # Menu segment here:
    while True:
        print("\n")
        print("Menu:")
        print("1. Problem 1a")
        print("2. Problem 1b")
        print("3. Problem 2")
        print("4. Problem 5")
        print("5. Quit")
        print("\n")

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
            print("Enter n: ")
            n3 = int(input())
            print("Enter k: ")
            k = int(input())
            problem2(n3, k)

        elif choice == "4":
            problem4a()
            N, E, D = problem4()
            print("RSA Keys Generated:")
            print("N:", N)
            print("E:", E)
            print("D:", D)

            message = input("Enter the plaintext message to encrypt: ")
            encrypted_message, decrypted_message = encrypt_and_decrypt_message(
                N, E, D, message
            )

            print("\nEncrypted Message:")
            print(encrypted_message)
            print("\nDecrypted Message:")
            print(decrypted_message)

        elif choice == "5":
            print("\nGoodbye.\n")
            break


if __name__ == "__main__":
    main()
