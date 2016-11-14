#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

i, j, k = input().strip().split(' ')
i, j, k = int(i), int(j), int(k)

def getReversedNum(num):
    numOfDigits = 0
    remainder = 0

    revNum = 0
    tmpNum = num
    while tmpNum > 0:
        remainder = tmpNum % 10

        revNum = (revNum * 10) + remainder
        tmpNum = tmpNum // 10
    else:
        return revNum

count = 0
for num in range(i, j + 1):
    revNum = getReversedNum(num)
    if abs(num - revNum) % k == 0:
        count += 1
print(count)
