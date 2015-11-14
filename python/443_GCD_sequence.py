'''
Let g(n) be a sequence defined as follows:
g(4) = 13,
g(n) = g(n-1) + gcd(n, g(n-1)) for n > 4.

The first few values are:

n		4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	...
g(n)	13	14	16	17	18	27	28	29	30	31	32	33	34	51	54	55	60	...
You are given that g(1 000) = 2524 and g(1 000 000) = 2624152.

Find g(10^15).
'''

from utils.utils import memoize
from utils.mymath import ext_gcd, egcd
from fractions import gcd
import pdb

# naive solution with memoization 
# requires too much memory and slow
@memoize
def g(n):
	if(n == 4):
		return 13
	else:
		x = g(n-1)
		return x + gcd(n, x)

def run_g():
	for i in range(4,10**15):
		if(i == 10**15):
			print(g(i))
		else:
			g(i)


# iterative, only save previous
# TOO SLOW
def g2(n):
	prev = 13
	cur = prev

	for i in range(4,n+1):
		if(i == 4):
			cur = 13
		else:
			cur = prev + gcd(i,prev)
		prev = cur

	return cur

def run_g2():
	with open('out.txt',mode='w', encoding='utf-8') as out:
		for i in range(4, 100000):
			out.write(str(g2(i)))
			out.write('\n')
			# print(i, g2(i))
	print('done')

run_g2()
# print(g2(10**6))

# using extended Euclidean,is slower
def g2_2(n):
	prev = 13
	cur = prev

	for i in range(4,n+1):
		if( i == 4):
			cur = 13
		else:
			g, a, b = ext_gcd(prev, i)
			cur = (1+a)* prev + b * i
		prev = cur

	return cur

def run_g2_2():
	for i in range(4, 20):
		print(i, g2_2(i))

# run_g2_2()
# print(g2_2(10**6))
