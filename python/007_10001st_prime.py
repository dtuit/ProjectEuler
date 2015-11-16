'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from eulerlib.primes import infiniteSieveOfEratosthenes

def nthPrime(n):
	primes = infiniteSieveOfEratosthenes()
	m = 1
	for i in primes:
		if m == n:
			return i
		m += 1

def solve():
	return nthPrime(10001)

if __name__ == '__main__':
	print(solve())