#!/usr/bin/env python

data = [line.rstrip() for line in open("input.txt", "r")]

x = 0
y = 0
for cmd in data:
    dir, dist = cmd.split()
    dist = int(dist)
    if dir == "forward":
        x += dist
    elif dir == "up":
        y -= dist
    else:
        y += dist
print(x*y)
