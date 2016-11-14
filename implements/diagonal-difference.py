#https://www.hackerrank.com/challenges/diagonal-difference
import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diagA = diagB = 0
for i in range(n):
    diagA += a[i][i]
    diagB += a[i][n - i - 1]
print(abs(diagA - diagB))
