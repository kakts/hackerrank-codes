#https://www.hackerrank.com/challenges/save-the-prisoner

# see the discussion https://www.hackerrank.com/challenges/save-the-prisoner/forum
#!/bin/python3

import sys

t = int(input().strip())
answerList = []
for i in range(t):
    n,m,s = input().strip().split(' ')
    n,m,s = [int(n),int(m),int(s)]

    surplus = m % n

    answer = None
    if surplus == 0:
        if s > 1:
            answer = s - 1
        else:
            answer = n
    elif surplus == 1:
        answer = s
    elif s + surplus - 1 > n:
        # if index number can be circulated
        answer = surplus - (n - s + 1)
    else:
        answer = s - 1 + surplus
    answerList.append(answer)

for data in answerList:
    print(data)
