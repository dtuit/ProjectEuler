'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from utils.primes import infiniteSieveOfEratosthenes

primes = infiniteSieveOfEratosthenes()

s = 0
p = next(primes)

while (p <= 2*10**6):
	s += p
	p = next(primes)

print(s)
