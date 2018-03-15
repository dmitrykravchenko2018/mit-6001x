#!/usr/bin/env python3

import string

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. 
    """

    sum = 0
    err = True
    for char in s:
    	if char.isdigit():
            sum += int(char)
            err = False
    if err:
    	raise ValueError('There are no digits in sting') 
    return sum

#print(sum_digits('a;35d4'), "Expected value : 12")
#print(sum_digits('a;0d0'), "Expected value : 0")

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    import collections
    l = []
    for el in t:
        if isinstance(el, collections.Iterable):
            l.append(max_val(el))
        else:
            l.append(el)
    return max(l)

#print(max_val((5, (1,2), [[1],[2]])), "Expected value : 5")
#print(max_val((5, (1,2), [[1],[9]])), "Expected value : 9")

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    assert(len(map_from) == len(map_to)), 'Each string should contain N letters'
    d = dict(zip(map_from, map_to))
    decoded = ""
    for char in code:
        decoded += d.get(char, char)
    return (d, decoded)

#print(cipher("abcd", "dcba", "dab"), "Expected output : ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')")

