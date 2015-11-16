'''
Find the sum of the even-valued terms, for fibonacci numbers under four million.
'''
def evenfibs():
    x = 0
    y = 1
    while True:
        if ((x & 1) == 0):
            yield x
        x, y = y, x + y

def solve():
    efib = evenfibs()

    max = 4*10**6
    s = 0

    for i in efib:
        if(i < max):
        	s += i
        else:
        	break

    return s

if __name__ == '__main__':
    print(solve())