#!/bin/python

import sys

def sumArrayNumbers(arr):
    sum = 0
    for n in arr:
        sum = sum + n
    return sum

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sumArrayNumbers(arr)