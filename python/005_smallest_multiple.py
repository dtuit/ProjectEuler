'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from itertools import count

def bruteForceSmallestMultiple(a, b):

    for i in count(start=1, step=1):
        check = True
        for j in range(a, b+1):
            if (i % j != 0):
                check = False
                break
        if check:
            return i

# print(bruteForceSmallestMultiple(1,20))

'''
Using 
        lcm(a,b) = |a * b| / gcd(a,b)
and     
        LCM(1,2) = x
        LCM(1,2,3) => LCM(x,3) = y
        LCM(1,2,3,4) => LCM(y,4) = z
'''

def lcm(a, b):
    def gcd(a, b):
         return a if b == 0 else gcd(b, a % b)
    return a * b // gcd(a, b)

def lcmSmallestMultiple(a , b):
    m = 1
    for n in range(a, b+1):
        m = lcm(m, n)
    return m

def solve():
    return lcmSmallestMultiple(1, 20)

if __name__ == '__main__':
    print(solve())