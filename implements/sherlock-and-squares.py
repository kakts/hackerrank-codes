#https://www.hackerrank.com/challenges/sherlock-and-squares

import sys
import math

t = int(input().strip())
answerList = []
for a0 in range(t):
    a,b = input().strip().split(' ')
    a,b = [int(a),int(b)]

    # if a = 3  b = 17
    # Those root number is 1.73....   and  4.12...  respectively.
    # We only find the squareable integer between 1.73... and 4.12...
    # Those integer numbers are 2,3,4
    # So, The answer is 3.
    answerList.append(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

for data in answerList:
    print(data)
