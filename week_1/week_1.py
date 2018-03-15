#!/usr/bin/env python

"""
 There are code for the problems listed as tasks for week 1
"""

"""
s = 'azcbobobegghakl'
counter = 0
for c in s:
    if c == 'a' or c =='e' or c == 'i' or c == 'o' or c == 'u':
        counter += 1
print(counter)
"""

"""
PROBLEM 2
Assume s is a string of lower case characters.

Write a program that prints the number of times 
the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
then your program should print 
>>> Number of times bob occurs is: 2

s = 'azcbobobegghakl'
sub = 'bob'
if s.islower():
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == sub:
            count += 1
print(count)
"""

"""
PROBLEM 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which 
the letters occur in alphabetical order. For example, 
if s = 'azcbobobegghakl', then your program should print
>>>Longest substring in alphabetical order is: beggh
"""

import string
s = 'azcbobobegghakl'

long_substr = ''
current_str = ''
prev_index = 0
if s.islower() and s.isalpha():
	for ch in s:
		if string.ascii_lowercase.find(ch) >= prev_index:
			current_str += ch
		else:
			current_str = ch
		prev_index = string.ascii_lowercase.find(ch)
		if len(current_str) > len(long_substr):
			long_substr = current_str
print(long_substr) 
