#!/bin/python3

import sys


n = int(input().strip())
for i in range(n):
    list = []
    text = ""
    for j in range(n):
        addChar = " "
        if j + 1 >= (n - i):
            # right pad
            addChar = "#"
        text += addChar
    print(text)
