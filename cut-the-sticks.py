#https://www.hackerrank.com/challenges/cut-the-sticks

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def cut(stickArr):
    size = len(stickArr)
    if size == 0:
        return
    # detarmine minimum number
    print(size)
    minimum = None
    for i in range(size):
        data = stickArr[i]
        if i == 0:
            minimum = data

        if minimum > data:
            minimum = data

    list = []
    for j in range(size):
        data = stickArr[j]
        if data != minimum:
            list.append(data - minimum)
    cut(list)

cut(arr)
