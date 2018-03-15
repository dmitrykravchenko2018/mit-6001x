#!/usr/bin/env python

from sympy import Symbol

x = Symbol('x')

f = x**2-5*x+27;
E = 0.01;
a = 0.0;
b = 4.0;
L = b - a
m = (a + b) / 2;
x1 = a + L / 4;
x2 = b - L / 4;

while L > E:
	f1 = f.subs(x,x1);
	fm = f.subs(x,m);
	f2 = f.subs(x,x2);
	if f1 >= fm:
		if fm > f2:
			a,m = m,x2;
			L = b - a;
			x1 = a + (L / 4);
			x2 = b - (L / 4);
		else:
			a,b = x1,x2;
			L = b - a;
			m = (a + b) / 2;
			x1 = a + (L / 4);
			x2 = b - (L / 4);
	else:
		b,m = m,x1;
		L = b - a;
		x1 = a + (L / 4);
		x2 = b - (L / 4);

print "Range is ",L
print "Answer is "
if f1 >= fm:
	if fm>f2:
		print x2, f2
	else:
		print m,fm
else:
	print x1,f1
