#https://www.hackerrank.com/challenges/sock-merchant
#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

# O(n) + O(n)
memberList = []
for i in range(len(c)):
    data = c[i]
    if memberList.count(data) == 0:
        memberList.append(data)

count = 0
for j in range(len(memberList)):
    ans = c.count(memberList[j]) // 2
    count += ans

print(count)
