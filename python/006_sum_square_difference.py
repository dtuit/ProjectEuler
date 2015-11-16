'''
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# https://oeis.org/A000330
def n_sumOfSqares(n):
    return n * (n+1)*(2*n+1)/6

# (n(n+1)/2)^2
def n_sumSquare(n):
    return int( ((n*(n+1))//2)**2 )

def solve():
    x1 = n_sumOfSqares(100) 
    x2 = n_sumSquare(100)
    return x2 - x1

if __name__ == '__main__':
    print(solve())