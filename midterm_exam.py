#!/usr/bin/env python3

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    ans = 0
    for x in range(1, k + 1):
    	ans += x
    	if ans == k:
    		return True
    return False

#print(is_triangular(6))
#print(is_triangular(10))
#print(is_triangular(7))

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = 'aeiou'
    tmp = s[:]
    for ch in s.lower():
    	if ch in vowels:
    		tmp = tmp.replace(ch, '')
    		tmp = tmp.replace(ch.upper(), '')
    return tmp

#print(print_without_vowels("This is great!"))
#print(print_without_vowels('Here is a simple sentence that makes sense. BYE.'))

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None 
    """
    tmp_set = set(L)
    while len(tmp_set) > 0:
    	res = max(tmp_set)
    	if (L.count(res) % 2) != 0:
    		return res
    	else:
    		tmp_set.remove(res)

#print(largest_odd_times([3,9,5,3,5,3]))
#print(largest_odd_times([2,2,4,4]))

def dict_invert(d):
    '''
    d: dict

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

    Returns an inverted dictionary according to the instructions above
    '''
    inverted_d = {}
    for k,v in d.items():
    	if v in inverted_d:
    		inverted_d[v].append(k)
    		inverted_d[v].sort()
    	else:
    		inverted_d[v] = [k]
    return inverted_d

#print(dict_invert({1:10, 2:20, 3:30, 4:30}))
#print(dict_invert({4:True, 2:True, 0:True}))
#print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function !!!!, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def evaluate(x, l = L):
    	res = 0
    	k = len(l) - 1
    	for n in l:
    		res += n * x ** k
    		k -= 1
    	return res

    return evaluate

#print(general_poly([1, 2, 3, 4])(10))

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
    	return False
    elif len(L1) == 0 and len(L2) == 0:
    	return (None, None, None)
    l1 = L1[:]
    max_num, val = 0, 0
    for elem in L2:
    	if elem in l1:
    		counter = l1.count(elem)
    		if counter > max_num:
    			max_num = l1.count(elem)
    			val = elem
    		l1.remove(elem)
    if len(l1) == 0:
    	return (val, max_num, type(val))
    else:
    	return False

#L1 = [1, 'b', 1, 'c', 'c', 1]
#L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation([1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c']))

#L1 = ['a', 'a', 'b']
#L2 = ['a', 'b']
print(is_list_permutation(['a', 'a', 'b'], ['a', 'b']))
print(is_list_permutation([], []))
