#!/usr/bin/env python3

import math

def polysum(n, s):
    '''
    n,s: positive integers
    
    n: number of polygon's sides
    s: side length

    returns: The sum of the area and square of the perimeter 
    of the regular polygon, rounded to 4 decimal places
    '''
    def area(n,s):
        '''
        n,s: positive integers

        returns: The area of a regular polygon
        '''
        return (0.25 * n * s**2) / math.tan(math.pi / n)

    def perimeter(n, s):
        '''
        n,s: positive integers
        
        returns: The perimeter of a polygon
        '''
        return n * s
    
    return round( area(n,s) + perimeter(n,s)**2, 4)