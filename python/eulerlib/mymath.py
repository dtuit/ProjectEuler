from .utils import memoize
import math

@memoize
def gcd(a, b):
    ''' Returns the greatest common divisor of a and b'''
    return a if b == 0 else gcd(b, a % b)

def ext_gcd(a, b):
    ''' Extended Eculidean algorithm for gcd 
        returns triple (g, x, y) such that for inputs a and b, 'ax + bx = gcd(a,b)'
    '''
    s, t, s1, t1 = 0,1, 1,0
    while a != 0:
        q, r = divmod(b,a)
        s2 = s-s1*q
        t2 = t-t1*q
        # print(a,b, q,r, s, s1,s2, t,t1,t2)
        s, s1 = s1, s2
        t, t1 = t1, t2
        b, a = a, r
    gcd = b
    return (gcd , s, t)

def factors(n):
    ''' Returns all factors of n'''
    factors = []
    if(n == 1):
        return [1]
    for i in range(1, int(n**0.5)+1):
        q, r = divmod(n,i)
        if(r == 0):
            factors.append(i)
            if( i != q):
                factors.append(q)
    return factors

def combination(n, k):
    '''
    n things taken k at a time without repetition
    product for i=1 to k; n+1-i/i
    '''
    res = 1
    for i in range(1,k+1):
        res *= ((n+1-i)/i) 
    return int(res)