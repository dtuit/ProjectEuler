'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def solve_naive():
    ans = 0
    max = 0
    for i in range(1, 10**6):
        n = i
        length = 0

        while n != 1:
            if n & 1:
                n = n*3 + 1
                length += 1
            else:
                n = int(n/2)
                length += 1
        if(length > max):
            max = length
            ans = i

    print(ans, max)

def solve():
    '''using a cache for previously found lengths'''
    ans = 0
    max = 0
    cache = {}
    for i in range(1, 10**6):
        n = i
        length = 0

        while n != 1:

            if n & 1:
                n = n*3 + 1
                length += 1
            else:
                n = int(n/2)
                length += 1

            if n in cache:
                length += cache[n]
                break

        cache[i] = length

        if(length > max):
            max = length
            ans = i

    return ans

if __name__ == '__main__':
    print(solve())