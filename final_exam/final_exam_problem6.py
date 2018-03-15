#!/usr/bin/env python3

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
        	self.vals[e] -= 1
        except KeyError:
        	return 0

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        return self.vals.get(e, 0)

    def __add__(self, other):
    	cp = Bag()
    	cp.vals = self.vals.copy()
    	for e,n in other.vals.items():
    		try:
    			cp.vals[e] += n
    		except:
    			cp.vals[e] = n
    	return cp

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self
        """
        try:
        	del self.vals[e]
        except KeyError:
        	pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise.
        """
        return e in self.vals
        

d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)
# 4:2
# 4:2

d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))
print(d1.count(4))
# 0
# 3

a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)
# 3:1
# 4:2

d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))