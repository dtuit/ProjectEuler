'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''

def n_largestProduct_s(num, n):
    l = len(num)
    s = 1
    for z in num[0:n]:
        s = s * z

    for i in range(1, l-n):
        m = 1
        for j in num[i:i+n]:
            m = m * j
        if s < m:
            s = m
    return s
    
def solve():
    txt_file = open("input/008.txt", "r")
    num = [int(i) for i in txt_file.read().replace('\n', '')]

    return n_largestProduct_s(num, 13)

if __name__ == '__main__':
    print(solve())