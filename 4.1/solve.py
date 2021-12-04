#!/usr/bin/env python

'''
0  1  2  3  4
5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
'''
wins = [ range(5),
         range(5,10),
         range(10,15),
         range(15,20),
         range(20,25),
         range(0,25,5),
         range(1,25,5),
         range(2,25,5),
         range(3,25,5),
         range(4,25,5)
        ]

# God I'm bad at parsing input
with open("input.txt", "r") as f:
    draw_nums = [int(num) for num in f.readline().rstrip().split(",")]
    
    count = 0
    boards = []
    curr_board = []
    for line in f:
        count += 1
        if count == 1:
            continue
        curr_board = curr_board + [(int(num), 0) for num in line.rstrip().split()]

        if count == 6:
            boards.append(curr_board)
            curr_board = []
            count = 0

# Solve problem yo
for num, i in zip(draw_nums, range(len(draw_nums))):
    
    # Update boards with curr num
    for b in boards:
        for entry, j in zip(b, range(len(b))):
            if entry[0] == num:
                b[j] = (num, 1)
                break

        # Don't check for wins until it is possible
        if i < 4:
            continue;

        # Check for win
        for w in wins:
            if sum([b[j][1] for j in w]) == 5:
                
                # For the longest time I was multiplying the sum of the winning row by the most recent number...
                # Make sure to read the problem :/
                unmarked_sum = sum([entry[0] for entry in b if entry[1] == 0])
                print(unmarked_sum * num)
                break
        else:
            continue
        break
    else:
        continue
    break
