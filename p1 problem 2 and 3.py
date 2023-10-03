#Adam E, Seth N
#problem 2
#The goal of this problem is to implement a modified primality test primality3: Given as
#input an integer N and confidence parameter k, first test if N is divisible by 3, 5, 7 or 11. If it
#is divisible by any of these numbers output("no"); else call primality2 with N and k as inputs.
#(This in turn calls primality algorithm that randomly chooses a (where 1 < a < N) and tests
#if a^(N-1) = 1(mod N) and repeats it k times to reduce the probability of error to 2^(-k).)
import random


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


testN = int(input("\nProblem 2: input n:"))
testk = int(input("\nProblem 2: input k:"))
if(primality3(testN, testk)) : print("yes")
else: print ("no")


#Given integers n and k, generate a random prime number P with n bits with a guarantee that P is a prime with probability at least 2**(-k).
#Implement a solution as follows: generate a random n-2 binary string and add 1 as the first and the last bit to create an n bit integer and convert it to decimal.
#(The reason for the first bit to be 1 is that we want the number to be odd. The last bit should be 1 since we want no leading 0's.)
#Then, call primality3 algorithm you in implemented in Problem 2 with n and k as inputs. (k is the second parameter in primality3 which is the number of times the Fermat's test is repeated.)
#Repeat calling primaility3 until it outputs 'yes'. At this point, you have found a prime number (with a probability at least 2**(-k)).
