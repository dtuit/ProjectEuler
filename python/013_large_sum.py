'''
Work out the first ten digits of the sum of the one-hundred 50-digit numbers in "res/013.txt".
'''
from functools import reduce

def solve():
	txt_file = open("input/013.txt", "r")
	num = sum([int(i) for i in txt_file])
	return(str(num)[0:10])

if __name__ == '__main__':
	print(solve())