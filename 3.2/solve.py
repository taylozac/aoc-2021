#!/usr/bin/env python

data = [line.rstrip() for line in open("input.txt", "r")]


def split(arr, idx):
    zero = []
    one = []
    for elem in arr:
        if elem[idx] == "0":
            zero.append(elem)
        else:
            one.append(elem)
    return zero, one


oxygen, co2 = split(data, 0)
if len(oxygen) < len(co2):
    temp = co2
    co2 = oxygen
    oxygen = temp


for i in range(1,len(data[0])):
    
    if len(oxygen) > 1:
        zero, one = split(oxygen, i)
        if len(one) < len(zero):
            oxygen = zero
        else:
            oxygen = one
    
    if len(co2) > 1:
        zero, one = split(co2, i)
        if len(one) < len(zero):
            co2 = one
        else:
            co2 = zero

print(int(oxygen[0], 2)*int(co2[0], 2))

