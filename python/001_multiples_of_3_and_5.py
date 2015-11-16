'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import math

def solve():
    a , b, n = 3, 5, 1000

    an = sum_k_multiples_n(a, n) 
    bn = sum_k_multiples_n(b, n) 
    abn = sum_k_multiples_n(15, n)

    return an + bn - abn

def sum_k_multiples_n(k, n):
    _n = math.floor((n-1)/k)
    kn = (( (k*_n)*(_n + 1) )/ 2)
    return kn


if __name__ == '__main__':
    print(solve())