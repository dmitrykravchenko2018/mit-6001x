#!/usr/bin/env python

from sympy import Symbol

"""
This is realisation of bisection method also called method Bolzano/
middle point method. In this particular case it is used as 
optimization method in order to find minimum of the given function.
Therefore it works with function's derivative!
"""

def sign(x):
	return (x > 0) - (x < 0)

x = Symbol('x')

f = x**2-5*x+27;
E = 0.01;
a = 0.0;
b = 4.0;

df = f.diff(x);
df_a = df.subs(x, a);
df_b = df.subs(x, b);
x_m = a + (b-a) / 2;
df_m = df.subs(x, x_m);

if sign(df_a) != sign(df_b):
	while abs(df_m) > E:
		x_m = a + (b-a) / 2;
		df_m = df.subs(x, x_m);
		if sign(df_a) == sign(df_m):
			a = x_m;
		elif sign(df_b) == sign(df_m):
			b = x_m;
f_m = f.subs(x, x_m)
print "x_min = %f f(x_min) = %f"%(x_m, f_m)

	
