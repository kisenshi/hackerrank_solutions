#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    maximum = None
    n_maximum = 0

    # It is kept track the maximum number and the number of times it has appeared
    for number in ar:
        if not maximum or number > maximum:
            maximum = number
            n_maximum = 1
        elif maximum == number:
            n_maximum = n_maximum + 1

    return n_maximum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))

result = birthdayCakeCandles(n, ar)
print(result)
