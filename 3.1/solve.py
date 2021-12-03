#!/usr/bin/env python

data = [line.rstrip() for line in open("input.txt", "r")]

total_1 = [0]*len(data[0])
for d in data:
    for i in range(len(d)):
        if d[i] == "1":
            total_1[i] += 1

gamma = ""
epsilon = ""
for pos in total_1:
    if pos > 500:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
