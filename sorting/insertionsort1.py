#https://www.hackerrank.com/challenges/insertionsort1

#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

e = a[n - 1]

def printArray(array):
    res = ""
    for i in range(len(array)):
        data = str(array[i])
        if i == len(array):
            res += data
        else:
            res += data + " "

    print(res)

for i in range(0, n):
    # 昇順ソートされた配列に対してインサートするため、配列の後ろからチェックしていく
    pos = n - i - 1
    if pos == 0:
        a[0] = e
    elif a[pos - 1] >= e:
        a[pos] = a[pos - 1]
    else:
        a[pos] = e
        printArray(a)
        break
    printArray(a)
