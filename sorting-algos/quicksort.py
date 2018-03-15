#!/usr/bin/env python3

def quicksort(arr):
	if len(arr) <= 1: return arr
	p = arr[0]
	return quicksort(filter(lambda x: x < p, arr[1:])) + [p] + quicksort(filter(lambda x: x >= p, arr[1:]))