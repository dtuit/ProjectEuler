'''
https://projecteuler.net/problem=12

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

from utils.mymath import factors
import itertools

def triangle_numbers():
	i = 1
	n = 0
	while True:
		n = n + i
		yield n
		i += 1

def solve():
	for i in triangle_numbers():
		f = factors(i)
		if( len(f) > 500):
			print(i, f)
			break

solve()
