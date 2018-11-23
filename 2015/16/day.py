"""
Advent of Code 2015 
"""
DAY = 16 

##### Functions #####
import re

detected_compounds = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

# Store input in a list
with open('input') as file:
    f = file.read().strip().split('\n')

# Format Data
pattern = r'^\w+ (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
aunt_sues = {}
for line in f:
    r = re.findall(pattern, line)
    aunt_sues[r[0][0]] = {}
    i = 1
    while i < len(r[0][1:]):
        aunt_sues[r[0][0]].update({r[0][i]: int(r[0][i+1])})
        i += 2


# Find aunt Sue: Part 1
for sue in aunt_sues:
    matches = len(aunt_sues[sue])
    match = 0
    for memory in aunt_sues[sue]:       
        if aunt_sues[sue][memory] == detected_compounds[memory]:
            match += 1
    if matches == match:
        my_sue = sue

# Find real aunt Sue: Part 2
for sue in aunt_sues:
    matches = len(aunt_sues[sue])
    match = 0
    for memory in aunt_sues[sue]:
        if memory == 'cats' or memory == 'trees':
            if aunt_sues[sue][memory] > detected_compounds[memory]:
                match += 1          
        elif memory == 'pomeranians' or memory == 'goldfish':
            if aunt_sues[sue][memory] < detected_compounds[memory]:
                match += 1
        elif aunt_sues[sue][memory] == detected_compounds[memory]:
            match += 1
    if matches == match:
        real_sue = sue

if __name__ == '__main__':
    part1 = my_sue
    part2 = real_sue

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
