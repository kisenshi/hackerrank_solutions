#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))

#The array is ordered
arr.sort()

# We obtain the sum of numbers in positions 1, 2 and 3
medium_sum = arr[1] + arr[2] + arr[3]

# The minumum sum will be adding the minimum, and the maximum adding the maximum
print str(medium_sum + arr[0]) + " " + str(medium_sum + arr[4])
