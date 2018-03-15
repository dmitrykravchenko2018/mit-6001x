#!/usr/bin/python

print "Hello World"

boolVar = True

if boolVar:
	print "true"
elif boolVar:
	print "Double true"
else: 
	print "False"

word = 'word' # they have the same meaning 
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "Carl"       # A string

print counter
print miles
print name

# Multiple assignment
a,b,c = 1,2,"john"
print a,b,c

#
s1 = "Hello"
s2 = "Python"

print s2+s1
print s1*2

#lists
print "LISTS"

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

print list1
del list1[2];
print "After deleting value at index 2 : "
print list1,"\n", len(list1)

# TUPLE 
# The differences between tuples and lists are, the tuples
# cannot be changed unlike lists and tuples use parentheses,
# whereas lists use square brackets.
print "TUPLE"

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

tup = ('physics', 'chemistry', 1997, 2000);

print tup
del tup;
print "After deleting tup : "
print tup