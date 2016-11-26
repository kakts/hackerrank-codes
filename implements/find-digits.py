#https://www.hackerrank.com/challenges/find-digits
#!/bin/python3

import sys


t = int(input().strip())
answerList = []
for a0 in range(t):
    n = int(input().strip())

    tmp = n
    traversedDigitList = []
    while tmp > 0:
        remainder = tmp % 10
        traversedDigitList.append(remainder)
        tmp = tmp // 10

    count = 0
    for digit in traversedDigitList:
        if digit == 0:
            continue
        elif n % digit == 0:
            count += 1
    answerList.append(count)

for data in answerList:
    print(data)
