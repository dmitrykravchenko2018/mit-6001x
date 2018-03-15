#!/usr/bin/env python

def sign(x):
	return (x > 0) - (x < 0)

from sympy import Symbol

x = Symbol('x')

f = x**2-5*x+27;
E = 0.01;
a = 0.0;
b = 4.0;

df = f.diff(x)
df_k = 100

while abs(df_k) > E:
	df_a = df.subs(x, a)
	df_b = df.subs(x, b)
	x_k = a - (df_a * (b - a) / (df_b - df_a))
	df_k = df.subs(x, x_k)
	if sign(df_a) != sign(df_k):
		b = x_k
	else:
		a = x_k

print "X min = %f f(x min) = %f" % (x_k, f.subs(x, x_k))

