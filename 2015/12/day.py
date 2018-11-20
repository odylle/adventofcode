"""
Advent of Code 2015 
"""
DAY = 12 

##### Functions #####
import json

class CountIntegers():
    pass

def traverse(node):
    if isinstance(node, list) or isinstance(node, dict):
        for key in node:
            if isinstance(node, dict):
                if count.red and CheckRed(node):
                    break
                key = node[key]
            traverse(key)
    else:
        if isinstance(node, int):
            count.total += node
        else:
            pass

def CheckRed(node):
    """
    Will return false if none of the direct values are 'red'
    """
    for key in node:
        if node[key] == 'red':
            return True


if __name__ == '__main__':
    with open ('input.json') as file:
        j = json.loads(file.read().strip())

    count = CountIntegers()
    # Part 1
    count.total = 0    
    count.red = False
    traverse(j)
    part1 = count.total
    # Part 2
    count.total = 0
    count.red = True
    traverse(j)
    part2 = count.total

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
