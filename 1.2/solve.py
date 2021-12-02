#!/usr/bin/env python

data = [int(line.rstrip()) for line in open("input.txt", "r")]

total = 0
prev = sum(data[0:3])
for i in range(1, len(data) - 2):
    curr = sum(data[i:i+3])
    if curr > prev:
        total += 1
    prev = curr
print(total)
