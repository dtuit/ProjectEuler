'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math
from eulerlib.mymath import gcd

# optimized naive solution 
def pythagorean_triples(max):
    for a in range(1, max+1):
        for b in range(a+1, max+1):
            s = a**2 + b**2
            c = int(s**0.5)
            if(s == c**2) and (c <= max):
                yield (a, b, c)

def special_pythagorean_triple():
    triples = pythagorean_triples(1000)
    m = 1
    while True:
        a,b,c = next(triples)
        if(a+b+c == 1000):
            return a*b*c
        m+=1

def solve():
    return special_pythagorean_triple()

# faster Solution
# a = (m^2 − n2^)*d, b = 2*m*n*d, c = (m^2 + n^2)*d,
def pythagorean_triples_faster(s):
    s2 = s/2
    mlimit = math.ceil(s2**0.5) -1
    for m in range(2, mlimit):
        if(s2 % m  == 0):
            sm = s2 / m
            while (sm % 2 == 0):
                sm = sm / 2
            if(m % 2 == 1 ):
                k = m+2
            else:
                k = m+1
            while(k < 2*m and k <= sm):
                if(sm % k == 0 and gcd(k,m) == 1):
                    d = s2 / (k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    return (a,b,c)
                k = k+2

def solve2():
    a, b, c = pythagorean_triples_faster(1000)
    return (a*b*c)

if __name__ == '__main__':
    print(solve2())