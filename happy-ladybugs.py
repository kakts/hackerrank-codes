#https://www.hackerrank.com/challenges/happy-ladybugs

#!/bin/python3

import sys

# check if ladybugs can be happy
def checkNonUnderScore(str):
    strLen = len(str)

    isLadyBugHappy = False
    for i in range(strLen):
        if i == 0 and strLen != 1:
            if str[i] == str[i + 1]:
                isLadyBugHappy = True
            else:
                isLadyBugHappy = False
                break
        elif i == strLen - 1:
            if str[i - 1] == str[i]:
                isLadyBugHappy = True
            else:
                isLadyBugHappy = False
                break
        elif str[i - 1] == str[i] or str[i] == str[i + 1]:
            isLadyBugHappy = True
    print(isLadyBugHappy)
    return isLadyBugHappy

def checkHappy(str):
    isLadyBugHappy = True
    for i in range(n):
        data = row[i]
        charCount = row.count(data)
        underScoreCount = row.count("_")
        if data == "_":
            continue

        if charCount == 1:
            isLadyBugHappy = False
            break
    return isLadyBugHappy

chatMap = {}
resultList = []
g = int(input().strip())
for gamuNum in range(g):
    n = int(input().strip())
    row = input().strip()

    isOk = True
    underScoreCount = row.count("_")
    if underScoreCount == 0:
        isOk = checkNonUnderScore(row)
    elif underScoreCount == n:
        resultList.append("YES")
        continue

    if isOk == False:
        resultList.append("NO")
        continue

    canBeHappy = checkHappy(row)
    if canBeHappy == True:
        resultList.append("YES")
        continue
    else:
        resultList.append("NO")
        continue

for res in resultList:
    print(res)
