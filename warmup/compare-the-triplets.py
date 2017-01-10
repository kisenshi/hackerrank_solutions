#!/bin/python

import sys

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

# Easier to create arrays to be able to have unique code for every comparison
a = [a0, a1, a2]
b = [b0, b1, b2]

# Ana and Bob scores are initialised to 0
ana_score = 0
bob_score = 0

for i in range(0, 3):
    if a[i] > b[i]:
        # If Ana's score is higher, it is added 1 to her final score
        ana_score = ana_score + 1
    elif b[i] > a[i]:
        # If Bob's score is higher, it is added 1 to his final score
        bob_score = bob_score + 1
        
# Final scores are printed
print(str(ana_score) + ' ' + str(bob_score))