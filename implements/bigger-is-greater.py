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

    # Find the pivotable position
    pivotPos = None
    for j in range(strLen):
        if j < strLen - 1 and strAsList[j] < strAsList[j + 1]:
            pivotPos = j
            break

    if pivotPos == None:
        answerList.append("no answer")
        continue

    # Find the suffix pivotable position
    pivotedPos = None
    for k in range(pivotPos, strLen):
        if pivotPos < k and strAsList[k] > strAsList[pivotPos]:
            pivotedPos = k

    tmp = strAsList[pivotPos]
    strAsList[pivotPos] = strAsList[pivotedPos]
    strAsList[pivotedPos] = tmp

    prefixList = []
    suffixList = []
    for l in range(strLen):
        data = strAsList[l]
        if l <= pivotPos:
            prefixList.append(data)
        else:
            suffixList.append(data)

    suffixList.sort()
    answerList.append("".join(prefixList + suffixList))

for data in answerList:
    print(data)
