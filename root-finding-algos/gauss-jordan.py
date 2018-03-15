#!/usr/bin/env python

# Creates a list containing 5 lists, each of 8 items, all set to 0
# https://snakify.org/lessons/two_dimensional_lists_arrays/
"""
rows, col = 5, 8;
Matrix = [[0 for x in range(col)] for y in range(rows)]
print Matrix

# another way
n = 3
m = 4
a = [[0] * m for i in range(n)]
"""

A = [[-0.87,	0.27,	-0.22,	-0.18,	-1.21],
	 [-0.21,	-1,		-0.45,	0.18,	0.33],
	 [0.12,		0.13,	-0.33,	0.18,	0.48],
	 [0.33,		-0.41,		0,	-1,		1.21]]

print A
print "len rows ", len(A)
print "len columns ", len(A[0])
print "A[0][0]", A[0][0]
print "-----"
print A[1:]
print "**********"
print A[1:][:]

print "Diagonal elements"
s = "".join(str(A[i][i]) for i in range(len(A)))
print s
# This one will return LIST of diagonal elements
print [A[i][i] for i in range(len(A))]


""" 
	The following realistion of Gauss-Jordan elimination algorithm 
	for given matrix calculates matrix in row echelon form (triangular form)

	Useful link about zip() and map()
	https://stackoverflow.com/questions/19017301/how-do-i-multiply-lists-together-using-a-function
	(can look in Saved pages)
"""
print "This is where it all begins..."

def gauss_jordan(matr):
	n = len(matr);
	m = len(matr[0]);

	for k in range(m-1):
		# Do for all rows below pivot:
		for i in range(k+1, n):			
			Cf = matr[i][k] / matr[k][k];
			# Do for all remaining elements in current row:
			matr[i] = map(lambda a,b: a-Cf*b, matr[i], matr[k]);
	return;

gauss_jordan(A);
for l in A:
	print l
