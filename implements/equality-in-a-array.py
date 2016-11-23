#https://www.hackerrank.com/challenges/equality-in-a-array
#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

counts = {}

for data in a:
    if data not in counts:
        counts[data] = 1
    else:
        counts[data] = counts[data] + 1

# Following code can be refactored
maximumNum = None
maximumKey = None
for k, v in counts.items():
    if maximumNum == None or maximumNum < v:
        maximumNum = v
        maximumKey = k

result = 0
if maximumNum == 1:
    result = n - 1
else:
    for k, v in counts.items():
        if maximumKey != k:
            result += v
print(result)
