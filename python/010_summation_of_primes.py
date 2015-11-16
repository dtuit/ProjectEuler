'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from eulerlib.primes import infiniteSieveOfEratosthenes


def solve():
    primes = infiniteSieveOfEratosthenes()

    s = 0
    p = next(primes)

    while (p <= 2*10**6):
        s += p
        p = next(primes)

    return s

if __name__ == '__main__':
    print(solve())
