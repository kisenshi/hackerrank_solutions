#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

# Diagonal 1 sum: Index change 00 11 ... (n-1)(n-1)
# Diagonal 2 sum: Index change 0(n-1) 1(n-2) ... (n-1)0
sum_diag1 = 0
sum_diag2 = 0
for i in range(0, n):
    sum_diag1 = sum_diag1 + a[i][i]
    sum_diag2 = sum_diag2 + a[i][n - 1 - i]

# It is calculated the diagonals diff and obtained the absolute value
diag_diff = abs(sum_diag1 - sum_diag2)

print(diag_diff)