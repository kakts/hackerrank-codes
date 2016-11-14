#https://www.hackerrank.com/challenges/2d-array?h_r=next-challenge&h_v=zen
#!/bin/python3

import sys

def getHourGlassSum(arr, x, y):
    sum = arr[x - 1][y - 1] + arr[x][y - 1] + arr[x + 1][y - 1] + arr[x][y] + arr[x - 1][y + 1] + arr[x][y + 1] + arr[x + 1][y + 1]
    return sum

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max = 0
for i in range(1, 5):
    for j in range(1, 5):
        sum = getHourGlassSum(arr, i, j)
        if sum > max:
            max = sum

print(max)
