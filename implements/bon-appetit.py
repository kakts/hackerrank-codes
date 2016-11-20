#https://www.hackerrank.com/challenges/bon-appetit

#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

a = [int(a_temp) for a_temp in input().strip().split(' ')]
chargedAmount = int(input().strip())

count = 0
for i in range(n):
    if i == k:
        continue
    count += a[i]

actualChargedAmount = count // 2

if chargedAmount == actualChargedAmount:
    print("Bon Appetit")
else:
    print(chargedAmount - actualChargedAmount)
