"""
Advent of Code 2015 
"""
DAY = 8

overhead = encoded = 0
with open('input') as file:
    for line in file:
        line = line.strip()
        overhead += len(line) - len(eval(line))
        # part 2 just adds extra characters
        # So we just count those?
        encoded += +2
        for c in line:
            if c == '\\' or c =='"':
                encoded += 1

if __name__ == '__main__':
    part1 = overhead
    part2 = encoded

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
