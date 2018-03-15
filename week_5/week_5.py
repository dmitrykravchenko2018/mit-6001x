#!/usr/bin/env python3

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
    	return self.x == other.x and self.y == other.y

    def __repr__(self):
    	return 'Coordinate({0},{1})'.format(self.x, self.y)

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
    	"""
    		Returns a new intSet containing elements that appear in both sets
    	"""
    	interSect = intSet()
    	for v in self.vals:
    		if other.member(v):
    			interSect.insert(v)
    	return interSect

    def __len__(self):
    	"""
    		Called to implement the built-in function len().
    		https://docs.python.org/3.3/reference/datamodel.html
    	"""
    	return len(self.vals)

def genPrimes():
	'''
		Genegator that returns the sequence of prime numbers
	'''
	print('Function start')
	primeList = []
	x = 1
	while True:
		x += 1
		prime = True
		for p in primeList:
			if (x % p) == 0:
				prime = False
				break
		if prime:
			primeList.append(x)
			yield x

g = genPrime()
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

def properDivisors(N):
    return [x for x in range(1,N-2) if not divmod(N,x)[1]]