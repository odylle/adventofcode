"""
Advent of Code 2015 
"""
DAY = 17

#Get Input
with open('input') as file:
    f = file.read().strip()

containers = sorted(list(map(int, f.split('\n'))), reverse=True)

EGGNOG = 150

from itertools import combinations

# Find largest number of containers that fit 150, so we can run combinations
volume = cc = 0
for c in sorted(containers):
    if volume + c < EGGNOG:
        cc += 1
        volume += c

max_c = cc


# Find smallest number of containers that fit 150, so we can run combinations
volume = cc = 0
for c in containers:
    if volume + c < EGGNOG:
        cc += 1
        volume += c

min_c = cc

# Find Combinations
filled = 0
for i in range(min_c, max_c+1):
    combis = combinations(containers, i)
    for c in combis:
        if sum(c) == 150:
            filled += 1

p1 = filled


# Number of combinations for smallest number
filled = 0
i = min_c
while True:
    for c in combinations(containers, i):
        if sum(c) == 150:
            filled += 1
    if filled > 0:
        break
    i += 1

p2 = filled 

##### Functions #####


if __name__ == '__main__':
    part1 = p1
    part2 = p2

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
