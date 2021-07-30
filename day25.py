# Day 25 - Running Time and Complexity

# Sample 1 - running time too long
def isprime(number):
    if number < 2:
        return("Not prime")
    else:
        for i in range(2,int(number/2)+1):
            if number%i == 0:
                return("Not prime")
                break
    
    return("Prime")
        
    
T = int(input().strip())
for i in range(T):
    print(isprime(int(input())))
  

# Sample 2 - running time just right
# Using logic that if a number is divisable by another number less or equal to the square root of the first number - it is NOT prime.

from math import sqrt

T = int(input())


def isprime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True


for i in range(T):
    n = int(input())
    
    if n >= 2 and isprime(n):
        print("Prime")
    else:
        print("Not prime")