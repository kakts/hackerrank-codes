#https://www.hackerrank.com/challenges/non-divisible-subset

import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
arrA = [int(a_temp) for a_temp in input().strip().split(' ')]

diviseList = []
for data in arrA:
    diviseList.append(data % k)

print(diviseList)

resList = []
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if (diviseList[i] + diviseList[j]) == k:
            count += 1
print(count)
"""
for i in range(n):
    isDivisible = True
    data1 = arrA[i]
    for j in range(n):
        print('--------i', i)
        print('--------j', j)
        if i == j:
            continue

        data2 = arrA[j]
        print('------data1 + data2', data1 + data2)
        print('------amari', (data1 + data2) % k)
        if (data1 + data2) % k != 0:
            print('------', data1 + data2)
            isDivisible = False
            break

    if isDivisible == False:
        count += 1
        resList.append(data1)
print(resList)
print(count)
"""
