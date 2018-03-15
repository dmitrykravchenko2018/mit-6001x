#!/usr/bin/python3

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    res = 0
    for v in aDict.values():
    	res += len(v)
    return res

#print(how_many(animals))
#print(animals.items())

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    tmp_max = 0
    res = ''
    for e in aDict:
        curr_len = len(aDict[e])
        if curr_len > tmp_max:
            tmp_max = curr_len
            res = e
    return res