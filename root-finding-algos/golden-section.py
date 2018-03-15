#!/usr/bin/env python3

""" 
This is simple realisation of golden-section search
algorithm 
"""
from sympy import Symbol

x = Symbol('x')

f = x**2-5*x+27;
E = 0.001;
a = 0.0;
b = 4.0;
t = 0.618;

L = b - a
x1 = a + L*(1-t)
x2 = a + L*t 

f1 = f.subs(x, x1)
f2 = f.subs(x, x2)

while L > E:
	if f1 > f2:
		a,x1,f1 = x1,x2,f2;
		L = b - a;
		x2 = b - L*(1-t);
		f2 = f.subs(x, x2);
	else:
		b,x2,f2 = x2,x1,f1;
		L = b - a;
		x1 = a + L*(1-t);
		f1 = f.subs(x, x1);

x_min = (a + b) / 2
f_min = f.subs(x, x_min)
print("Answer is", f_min)
