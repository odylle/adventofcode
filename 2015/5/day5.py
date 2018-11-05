"""
Advent of Code 2015: Day 5 
"""
DAY = 5

# Get input
with open('input') as file:
    input = (file.read()).strip()


##### Part 1: Helper Functions #####
def HasVowels(line):
    vowels = 'aeiou'
    vowel_count = 0
    for letter in line:
        if letter in vowels:
            vowel_count += 1
            if vowel_count == 3:
                return True

def HasDoubles(line):
    for i in range(len(line[:-1])):
        if line[i] == line[i+1]:
            return True

def IsNaughty(line):
    naughty_list = ['ab','cd','pq','xy']
    for badstring in naughty_list:
        if badstring in line:
            return True

##### Part 1 #####
def NiceLines(input):
    nice = 0
    for line in input.split():
        vowels = HasVowels(line)
        doubles = HasDoubles(line)
        naughty = IsNaughty(line)
        if vowels and doubles and not naughty:
            nice += 1
    return nice

part1 = NiceLines(input)
##### Part 2: Helper Functions #####
def HasComboString(line):
    for i in range(len(line[:-2])):
        combo = line[i]+line[i+1]
        if combo in line[i+2:]:
            return True

def HasRepeat(line):
    for i in range(len(line[:-2])):
        if line[i] == line[i+2]:
            return True

##### Part 2 #####
def MoreNiceLines(input):
    nice = 0
    for line in input.split():
        combo = HasComboString(line)
        repeat = HasRepeat(line)
        if combo and repeat:
            nice += 1
    return nice

part2 = MoreNiceLines(input) 

if __name__ == '__main__':
    print("Day %s Part 1: %s" % (DAY, part1,))
    print("Day %s Part 2: %s" % (DAY, part2,))
