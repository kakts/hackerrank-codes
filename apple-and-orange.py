#https://www.hackerrank.com/challenges/apple-and-orange
import sys

s,t = input().strip().split(' ')
a,b = input().strip().split(' ')
m,n = input().strip().split(' ')
mlist = input().strip().split(' ')
nlist = input().strip().split(' ')

mCount = 0
nCount = 0
s = int(s)
t = int(t)
for mData in mlist:
    pos = int(a) + int(mData)
    if (s <= pos and pos <= t):
        mCount += 1

for nData in nlist:
    pos = int(b) + int(nData)
    if (s <= pos and pos <= t):
        nCount += 1
print(mCount)
print(nCount)
