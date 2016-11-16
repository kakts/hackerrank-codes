#https://www.hackerrank.com/challenges/bigger-is-greater

import sys

t = int(input().strip())
a = []

answerList = []
replacedStr = []
for i in range(t):
    aStr = input().strip()
    strLen = len(aStr)

    strAsList = []
    for i in range(strLen):
        strAsList.append(aStr[i])

    firstChar = aStr[0]
    if aStr.count(firstChar) == strLen:
        answerList.append("no answer")
        continue
    positionCount = strLen - 2

    changeable = False
    while positionCount >= 0:
        if strAsList[positionCount] < strAsList[positionCount + 1]:
            tmp = strAsList[positionCount]
            strAsList[positionCount] = strAsList[positionCount + 1]
            strAsList[positionCount + 1] = tmp
            changeable = True
            break
        positionCount -= 1

    frontStr = []
    afterStr = []
    for k in range(strLen):
        if k <= positionCount:
            frontStr.append(strAsList[k])
        else:
            afterStr.append(strAsList[k])
    afterStr.sort()

    replacedStr = frontStr + afterStr
    print("--", replacedStr, positionCount)
    if changeable == False:
        answerList.append("no answer")
    else:
        answerList.append("".join(replacedStr))
for data in answerList:
    print(data)
