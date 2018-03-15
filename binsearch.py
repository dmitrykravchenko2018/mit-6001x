#!/usr/bin/env python

def binary_search(lst, x):
	l = 0
	r = len(lst)
	while (r - l) > 1:
		m = l + (r - l) // 2 
		""" In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2.
			In Python 3, they made the / operator do a floating-point 
			division, and added the // operator to do integer division.
		"""
		if lst[m] <= x:
			l = m
		else:
			r = m
	return l if lst[l] == x else None # if the element is not found then return None

def bin_search(lst, x):
	lo, hi = 0, len(lst)
	while lo <= hi:
		m = lo + (hi - lo) // 2
		if x < lst[m]:
			hi = m - 1
		elif x > lst[m]:
			lo = m + 1
		else:
			return m;

lst = sorted([int(x) for x in raw_input('Please input the row: ').split(" ")])
x = int(input('Element to find: '))
print "Sorted list", lst 
print "Boundary search elem index", binary_search(lst, x)
print "Standart bin search elem index", bin_search(lst, x)
