def find_smallest_j(n):
    j = 1
    sum1 = 0
    while sum1 < n:
        sum1 += 1 / j
        j += 1
    return j





"""
import random


# gcd function here:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Function to compute modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Function to generate our RSA keys:
def generate_rsa_keys():
    # Choose two distinct prime numbers, p and q
    p = random.randint(100, 200)
    q = random.randint(200, 300)

    # Compute n (modulus)
    n = p * q

    # Calculate Euler's totient function here:
    phi = (p - 1) * (q - 1)

    # Choose a public exponent (E) such that 1 < E < phi and gcd(E, phi) == 1
    E = random.randint(2, phi - 1)
    while gcd(E, phi) != 1:
        E = random.randint(2, phi - 1)

    # Calculate the private exponent (D) using the modular multiplicative inverse
    D = mod_inverse(E, phi)

    return E, D, n


# Function to encrypt a message using RSA
def encrypt_message(M, E, n):
    return pow(M, E, n)


# Function to decrypt a message using RSA
def decrypt_message(C, D, n):
    return pow(C, D, n)


# Main function
def main():
    # Generate RSA keys
    E, D, n = generate_rsa_keys()

    # Message to be encrypted
    M = random.randint(1, n - 1)

    # Encrypt the message
    C = encrypt_message(M, E, n)

    # Decrypt the message
    decrypted_message = decrypt_message(C, D, n)

    # Print the original message, encrypted message, and decrypted message
    print("Original Message (M):", M)
    print("Encrypted Message (C):", C)
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()
"""
