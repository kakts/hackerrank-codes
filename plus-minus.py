#https://www.hackerrank.com/challenges/diagonal-difference
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
nega = 0
zero = 0
for data in arr:
    if data > 0:
        pos += 1
    elif data == 0:
        zero += 1
    else:
        nega += 1

print(format(pos / n, '.6f'))
print(format(nega / n, '.6f'))
print(format(zero / n, '.6f'))
