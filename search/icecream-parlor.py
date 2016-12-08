#https://www.hackerrank.com/challenges/icecream-parlor
WIP
#!/bin/python3

import sys

t = int(input().strip())
answerList = []
for i in range(t):
    m = int(input().strip())
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    sum = 0
    resList = []
    for j in range(n):
        data = arr[j]
        # if data exceeded the value of m, it should be skipped
        if m <= data:
            continue
        elif m < (sum + data):
            continue

        sum += data
        resList.append(str(j + 1))
        if len(resList) == 2:
            break
    answerList.append(resList)

for res in answerList:
    print(" ".join(res))
