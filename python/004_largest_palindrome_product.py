'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# check all unique combinations of length n x m numbers 
def bruteforcePalindrome(n , m):
    lp = -1
    a = 10**(n-1)
    b = (10**n)-1

    for i in range(a, b):
        for j in range(i, b+1):
            x = i * j
            sx = str(x)
            if ( sx[::-1] == sx ) and ( x > lp):
                lp = x

    return lp

# check all unique combinations of length n x m numbers counting downwards
def bruteforcePalindrome_reversed(n , m):
    lp = -1
    a = 10**(n-1)
    b = (10**n)

    for i in reversed(range(a, b)):
        for j in range(a, i+1)[::-1]:
            x = i * j
            sx = str(x)
            if ( sx[::-1] == sx ):
                if( x > lp):
                    lp = x
                else:
                    break
    return lp

print(bruteforcePalindrome(3, 3))
print()
print(bruteforcePalindrome_reversed(3, 3))

