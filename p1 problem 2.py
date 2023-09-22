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
    if((a^(N-1))%N == 1 % N ):
        return True
    else:
        return False

def primality2(N, k):
    result = False
    for i in range(k):
        result = primality(N)
        if (result == True) : return result
    
    return result


def primality3(N, k):
    #int N and confidence prarameter k
    #output: true/false
    
    if(N % 3 == 1):
        return False
    elif(N % 5 == 1):
        return False
    elif(N % 7 == 1):
        return False
    elif(N % 11 == 1):
        return False
    
    return primality2


if(primality3(18, 5)) : print("yes")
else: print ("no")
    

