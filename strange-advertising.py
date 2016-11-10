#https://www.hackerrank.com/challenges/strange-advertising

import sys
import math

n = int(input().strip())

def get_amount(amount):
    return math.floor(amount / 2)


amount = 5
result = 0
for i in range(n):
    if i != 0:
        amount *= 3
    amount = get_amount(amount)
    result += amount
print(result)
