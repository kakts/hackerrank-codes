#https://www.hackerrank.com/challenges/kangaroo?h_r=next-challenge&h_v=zen
import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if x1 == x2:
    print("YES")
if v1 == v2:
    print("NO")
elif (x1 > x2 and v1 > v2):
    print("NO")
elif (x2 > x1 and v2 > v1):
    print("NO")
elif ((x1 - x2) % (v2 - v1) == 0):
    print("YES")
elif ((x2 - x1) % (v1 - v2) == 0):
    print("YES")
else:
    print("NO")
