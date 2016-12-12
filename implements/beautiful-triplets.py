#https://www.hackerrank.com/challenges/beautiful-triplets

#!/bin/python3

import sys

n,d = input().strip().split(' ')
n,d = [int(n),int(d)]

a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        if a[j] - a[i] > d:
            break
        elif a[j] - a[i] < d:
            continue
        for k in range(j + 1, n):
            if a[k] - a[j] > d:
                break
            elif a[k] - a[j] < d:
                continue

            count += 1
print(count)
