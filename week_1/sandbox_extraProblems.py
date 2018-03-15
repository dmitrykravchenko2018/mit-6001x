#!/usr/bin/env python3

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    assert(base > 1 and num > 0), 'Wrong parameters'
    exp = 0
    n = 1
    while n < num:
    	exp += 1
    	n *= base
    n2 = n // base
    if abs(n - num) < abs(n2 - num):
    	return exp
    return exp - 1

print(closest_power(3,12), "returns 2")
print(closest_power(4,12), "returns 2")
print(closest_power(4,1), "returns 0")
print(closest_power(2, 192.0), " Expected output : 7")