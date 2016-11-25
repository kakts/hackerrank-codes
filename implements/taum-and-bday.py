# https://www.hackerrank.com/challenges/taum-and-bday

#!/bin/python3

import sys


t = int(input().strip())
answerList = []
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    count = 0
    if x > y + z:
        count += b * (y + z)
    else:
        count += b * x

    if y > x + z:
        count += w * (x + z)
    else:
        count += w * y
    answerList.append(count)

for data in answerList:
    print(data)
