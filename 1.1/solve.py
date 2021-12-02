#!/usr/bin/env python

data = [int(line.rstrip()) for line in open("input.txt", "r")]

total = 0
for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        total += 1
print(total)
