#!/usr/bin/env python

data = [line.rstrip() for line in open("input.txt", "r")]

x = 0
y = 0
aim = 0
for cmd in data:
    dir, dist = cmd.split()
    dist = int(dist)
    if dir == "forward":
        x += dist
        y += aim * dist
    elif dir == "up":
        aim -= dist
    else:
        aim += dist
print(x*y)
