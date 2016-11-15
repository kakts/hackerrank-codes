#https://www.hackerrank.com/challenges/repeated-string
import sys

s = input().strip()
n = int(input().strip())

lenS = len(s)
countOfA = s.count("a")

quotient = n // lenS
remainder = n % lenS

countOfRemainder = 0
for i in range(remainder):
    data = s[i]
    if data == "a":
        countOfRemainder += 1

print(countOfA * quotient + countOfRemainder)
