'''
Work out the first ten digits of the sum of the one-hundred 50-digit numbers in "res/013.txt".
'''
from functools import reduce

txt_file = open("res/013.txt", "r")

num = sum([int(i) for i in txt_file])

print(str(num)[0:10])