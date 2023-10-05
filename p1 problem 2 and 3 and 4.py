#Adam E, Seth N
#problem 2, 3, 4

#problem 2
#The goal of this problem is to implement a modified primality test primality3: Given as
#input an integer N and confidence parameter k, first test if N is divisible by 3, 5, 7 or 11. If it
#is divisible by any of these numbers output("no"); else call primality2 with N and k as inputs.
#(This in turn calls primality algorithm that randomly chooses a (where 1 < a < N) and tests
#if a^(N-1) = 1(mod N) and repeats it k times to reduce the probability of error to 2^(-k).)
import random
from math import *

def primality(N):
    #input: positive int N
    #output: true/false
    
    #pick a positive int a<N at random
    a = random.randint(1, N)

    if((a**(N-1)) % N == (1 % N)): return True
    else: return False

def primality2(N, k):
    
    for i in range(k):
        result = primality(N)
        if (result == False) : return result
    
    return result

def primality3(N, k):
    #int N and confidence prarameter k
    #output: true/false
    
    if(N == 2 or N == 3 or N == 5 or N == 7 or N == 11): return True
    if(N % 2 == 0): return False
    if(N % 3 == 0): return False
    if(N % 5 == 0): return False
    if(N % 7 == 0): return False
    if(N % 11 == 0): return False
    
    return primality2


def problem2():
    testN = int(input("\nProblem 2: input n:"))
    testk = int(input("\nProblem 2: input k:"))
    if(primality3(testN, testk)) : print("yes")
    else: print ("no")


#problem 3
#Given integers n and k, generate a random prime number P with n bits with a guarantee that P is a prime with probability at least 2**(-k).
#Implement a solution as follows: generate a random n-2 binary string and add 1 as the first and the last bit to create an n bit integer and convert it to decimal.
#(The reason for the first bit to be 1 is that we want the number to be odd. The last bit should be 1 since we want no leading 0's.)
#Then, call primality3 algorithm you in implemented in Problem 2 with n and k as inputs. (k is the second parameter in primality3 which is the number of times the Fermat's test is repeated.)
#Repeat calling primaility3 until it outputs 'yes'. At this point, you have found a prime number (with a probability at least 2**(-k)).

def randomnumber(n):
    #input: n is number of bits in the binary number
    #output: random odd int in decimal
    binarynumber = '1'

    for i in range(n-2): binarynumber = binarynumber + random.choice(['0','1'])
    binarynumber = binarynumber + '1'
    
    return int(binarynumber, 2)


def problem3():
    
    randomN = int(input("\nProblem 3: input n:"))
    testk = int(input("\nProblem 3: input k:"))
    
    isprime = False
    while not isprime:
        testN = randomnumber(randomN)
        isprime= primality3(testN, testk)
        
    print(str(testN) + ' is prime')


def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

#problem 4
#Given integers n and k, call the algorithm for Problem 3 (with n and k as inputs) to generate
#two primes p and q with n bits each, and use them to generate the encryption keys E and the
#decryption key D. After computing p and q, compute N = pq. Then, find a random 10 bit
#integer E such that gcd (E, (p - 1)(q - 1)) = 1. Next, find D such that DE = 1 (mod N)
#using extended Euclid's algorithm. Output N, E and D.

def problem4():
    
    randomN = int(input("\nProblem 4: input n:"))
    testk = int(input("\nProblem 4: input k:"))
    
    isprime = False
    while not isprime:
        testN = randomnumber(randomN)
        isprime= primality3(testN, testk)
    p = testN
    
    isprime = False
    while not isprime:
        testN = randomnumber(randomN)
        isprime= primality3(testN, testk)
    q = testN
    
    N = p * q
    relativelyprime = False
    while not relativelyprime:
        E = ''
        for i in range(10): E = E + random.choice(['0','1'])
        E = int(E, 2)
        if (gcd(E, (p - 1)*(q - 1)) == 1): relativelyprime = True
    
    D = E**-1 % (p - 1)*(q - 1)
    
    print(N, ' ', E, ' ' , D)
    return N, E, D
    
problem4()