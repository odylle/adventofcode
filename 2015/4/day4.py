"""
Advent of Code 2015: Day 4
"""
from hashlib import md5
DAY = 4

# Get input
with open('input') as file:
    input = (file.read()).strip()


##### Part 1 #####
def FindCoin(input, multiplier):
    number = 0
    check = False
    found = '0'*multiplier
    while check == False:
        number += 1
        search = md5((input+(str(number))).encode('utf-8'))        
        if search.hexdigest()[0:multiplier] == found:
            check = True        
    return number

part1 = FindCoin(input, 5)
##### Part 2 #####

part2 = FindCoin(input, 6)

if __name__ == '__main__':
    print("Day %s Part 1: %s" % (DAY, part1,))
    print("Day %s Part 2: %s" % (DAY, part2,))
