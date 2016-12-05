# https://www.hackerrank.com/challenges/tutorial-intro
#!/bin/python3

import sys

v = int(input().strip())
n = int(input().strip())
list = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in range(n):
    if list[i] == v:
        print(i)
        break
