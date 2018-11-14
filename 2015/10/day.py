"""
Advent of Code 2015 
"""
DAY = 10

##### Functions #####
 ##### Part 1
def SplitForLookToSay(number):
    digits = []
    for i in range(len(number)):
        digit = number[i]
        if i > 0:
            if digits[-1][-1] == number[i]: 
                new = digits[-1]+number[i]
                del digits[-1]
                digits.append(new)
            else:
               digits.append(digit) 
        else:
            digits.append(digit)
    return digits

def LookToSay(digits):
    say = ""
    for digit in digits:
        say = say+str(len(digit))+digit[0]
    return say

 ##### Part 2
def BetterLookToSay(number):
    i = 0
    indexcount = 1
    sequence = ''
    while i < len(number):
        while True:
            if i+indexcount == len(number):
                sequence = sequence+str(indexcount)+number[i]
                i += indexcount
                break
            if number[i+indexcount] == number[i]:
                indexcount += 1
            else:
                sequence = sequence+str(indexcount)+number[i]
                i += indexcount
                indexcount = 1
                break
    return sequence

"""
Fun story: I thought to rewrite Part 1 as it seemed to take forever to 
find the answer. Turns out.. Both are about it even when it comes to
performance.
I have seen solutions using regex, which was quicker.
"""


if __name__ == '__main__':
    input = 3113322113 # Never mind importing it...
    say = str(input)
    for i in range(40):
        look = SplitForLookToSay(str(say))
        say = LookToSay(look)
    part1 = len(say)
    
    say = str(input)
    for i in range(50):
        say = BetterLookToSay(str(say))
    part2 = len(say)

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
