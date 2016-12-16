#https://www.hackerrank.com/challenges/service-lane

#!/bin/python3

import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]

answer = []
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]

    minimum = None
    for k in range(i, j + 1):
        if k == i or minimum > width[k]:
            minimum = width[k]

    answer.append(minimum)

for data in answer:
    print(data)
