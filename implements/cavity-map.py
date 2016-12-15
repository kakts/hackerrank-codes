#https://www.hackerrank.com/challenges/cavity-map

#!/bin/python3

import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)

answerGrid = []
for i in range(0, n):
    if i == 0 or i == n - 1:
        answerGrid.append(grid[i])
        continue

    rowStr = ""
    for j in range(0, n):
        if j == 0 or j == n - 1:
            rowStr += grid[i][j]
            continue

        data = int(grid[i][j])
        if data > int(grid[i - 1][j]) and data > int(grid[i][j - 1]) and data > int(grid[i][j + 1]) and data > int(grid[i + 1][j]):
            rowStr += "X"
        else:
            rowStr += grid[i][j]

    answerGrid.append(rowStr)

for k in range(len(answerGrid)):
    print(answerGrid[k])
