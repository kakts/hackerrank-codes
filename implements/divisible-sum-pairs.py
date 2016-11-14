#https://www.hackerrank.com/challenges/divisible-sum-pairs
#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

res = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % k == 0:
            res += 1
print(res)
