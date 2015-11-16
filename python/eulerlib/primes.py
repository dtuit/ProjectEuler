def infiniteSieveOfEratosthenes():
    '''SieveOfEratosthenes Generator for primes p, for 0 < p < inf '''
    sieve = {}
    q = 2
    while True:
        if q not in sieve:
            yield q
            sieve[q * q] = [q]
        else:
            for p in sieve[q]:
                sieve.setdefault(p + q, []).append(p)

            del sieve[q]
        q += 1    

def n_primes(n):
    '''Returns the first n primes'''
    primeGen = infiniteSieveOfEratosthenes()
    primes = []
    for i in range(0,n):
        primes.append(next(primeGen))
    return primes

def primes_under_n(n):
    '''Returns all primes less or equal to n'''
    primes = []
    for x in infiniteSieveOfEratosthenes():
        if(x > n):
            return primes
        primes.append(x)
