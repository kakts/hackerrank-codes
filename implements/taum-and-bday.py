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

    if b == w:
        if (2 * x + z) < y:
            answerList.append(b * (2 * x + z))
        elif x > (2 * y + z):
            answerList.append(w * (2 * y + z))
        else:
            answerList.append(b * x + w * y)
        continue

    isBExpensive = False
    if b > w:
        if b * x > w * (x + z):
            # if exchanging items could be cheaper
            answerList.append(w * (y + y + z))
        else:
            answerList.append(b * x + w * y)
    else:
        if w * y > b * (y + z):
            # if exchanging items could be cheaper
            answerList.append(b * (x + x + z))
        else:
            answerList.append(b * x + w * y)

for data in answerList:
    print(data)
