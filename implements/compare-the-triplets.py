#https://www.hackerrank.com/challenges/compare-the-triplets

import sys

a0,a1,a2 = input().strip().split(' ')
arrA = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
arrB = [int(b0),int(b1),int(b2)]

pointA = pointB = 0

for i in [0, 1, 2]:
    # subtract dataA dataB
    sub = arrA[i] - arrB[i]
    if sub > 0:
        pointA += 1
    elif sub < 0:
        pointB += 1

print(str(pointA) + " " + str(pointB))
