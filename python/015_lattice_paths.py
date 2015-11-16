'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

from eulerlib.mymath import combination

def solve():
    n,m = 20,20
    # (n right paths + m down paths) choose n disregarding order
    return combination(n+m, n)

if __name__ == '__main__':
    print(solve())