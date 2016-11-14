#https://www.hackerrank.com/challenges/arrays-ds

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = ""
for i in range(n):
    result = result + str(arr[n - i -1])
    if i != n - 1:
        result = result + " "
print(result)
