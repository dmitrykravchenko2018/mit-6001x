#!/usr/bin/env python

"""
Simple implementation of Newton-Raphson method
also known as tangent method
"""

from sympy import Symbol

x = Symbol('x')

f = x**2-5*x+27;
E = 0.01;
x0 = 0.0;

df = f.diff(x)
ddf = df.diff(x)

while True:
	x1 = x0 - (df.subs(x,x0) / ddf.subs(x, x0));
	if abs(df.subs(x, x1)) < E:
		print "X min = %f | f(X min) = %f" % (x1, f.subs(x, x1))
		break
	x0 = x1;

