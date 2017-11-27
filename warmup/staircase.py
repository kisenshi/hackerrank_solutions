#!/bin/python

import sys

n = int(raw_input().strip())

if n > 0:
    # right aligned the # the lenght of the staircase
    step = '#'.rjust(n)
    print step

    step_l = list(step)
    i = n - 2

    # Steps are added each time until the lenght is done
    while i >= 0:
        step_l[i] = '#'
        print ''.join(step_l)
        i = i - 1
