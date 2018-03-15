#!/usr/bin/env python3

"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
"""

def guess_num():
	"""
	Guess my number task
	# 0 <= x < 100
	"""
	lo, hi = 0, 100

	print("Please think of a number between 0 and 100!")
	while lo <= hi:
		m = lo + (hi - lo) // 2
		print("Is your secret number {0}?".format(m))
		ch = input("Enter 'h' to indicate the guess is too high.\
			Enter 'l' to indicate the guess is too low.\
			Enter 'c' to indicate I guessed correctly. ")
		if ch == 'h':
			hi = m
		elif ch == 'l':
			lo = m
		elif ch == 'c':
			print("Game over. Your secret number was: {0}".format(m))
			break
		else:
			print("Sorry, I did not understand your input.")	


# Exercise: gcd iter

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        div = b
    else:
        div = a
    while not ((a % div == 0) and (b % div == 0) or div == 1):
    	div -= 1
    return div  
    
#print("This is ANSWER !!", gcdIter(2, 12))
#print("This is ANSWER !!", gcdIter(1071, 462))
#print("This is ANSWER !!", gcdIter(17, 11))

def gcd(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    Uses Euclidean algorithm
    '''
    remainder = 0;
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    Uses Euclidean algorithm
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def fib(n):
	'''
	'''
	if n == 1:
		return 1
    elif n == 2:
        return 2
	else:
		return fib(n-1) + fib(n-2)


def isPalindrome(s):
	
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans += c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])
	return isPal(toChars(s))

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    lo, hi = 0, len(aStr)
    if len(aStr) == 0:
        return False
    
    m = lo + (hi - lo) // 2
    if char < aStr[m]:
        return isIn(char, aStr[:m])
    elif char > aStr[m]:
        return isIn(char, aStr[m + 1:])
    else:
    	return char == aStr[m]

print(isIn('a', ''))
print(isIn('e', 'cehkx'))
print(isIn('n', 'fnoz'))
print(isIn('s', 'cdhinopqqqswyyz'))
print(isIn('r', 'u'))




import math

def polysum(n, s):
    '''
    Here's a lambda version of the function:
    polysum = lambda n, s: round((0.25 * n * s**2) / __import__("math").tan(__import__("math").pi / n) + (n * s)**2, 4)
    
    returns: the sum of the area and square of the perimeter 
    of the regular polygon, rounded to 4 decimal places
    '''
    def polygonArea(n,s):
        '''
        n,s: positive integers
        n: number of polygon's sides
        s: side length
        
        returns: The area of a regular polygon
        '''
        return (0.25 * n * s**2) / math.tan(math.pi / n)
    def polygonPerimeter(n, s):
        '''
        n,s: positive integers
        
        n: number of polygon's sides
        s: side length
        
        returns: The perimeter of a polygon
        '''
        return n * s
    
    return round(polygonArea(n,s) + polygonPerimeter(n,s)**2, 4)
