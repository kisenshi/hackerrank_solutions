#!/bin/python

import sys

def obtain_fraction(n_numbers, total):
    return (n_numbers/total)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# [positives, negatives, 0]
types = [0, 0, 0]

# Obtained the number of positives, negatives and zeros
for x in arr:
    if x > 0:
        # positives
        types[0] = types[0] + 1
    elif x < 0:
        #negatives 
        types[1] = types[1] + 1
    else:
        # zeroes
        types[2] = types[2] + 1
        
# Percentages are obtained and printed
float_n = float(n)

for x in types:
    print "%.6f" % obtain_fraction(x, float_n)
