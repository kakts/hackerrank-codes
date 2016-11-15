#https://www.hackerrank.com/challenges/jumping-on-the-clouds

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

jumpCount = 0
position = 0

while position < n - 1:
    if (position + 2) <= (n - 1) and c[position + 2] == 0:
        position += 2
    elif (position + 1) <= (n - 1) and c[position + 1] == 0:
        position += 1
    jumpCount += 1
print(jumpCount)
