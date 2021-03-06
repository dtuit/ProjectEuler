'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from eulerlib.primes import infiniteSieveOfEratosthenes

def largestPrimeFactor(max):
    primes = infiniteSieveOfEratosthenes()
    p = next(primes)

    while(max >= p):
        if max % p == 0:
            lpf = p
            max = max / p
        else:
            p = next(primes)
    return lpf

def solve():
    n = 600851475143
    return largestPrimeFactor(n)

if __name__ == '__main__':
    print(solve())