"""
Advent of Code 2015: Day 5 
"""
DAY = 5

# Get input
with open('input') as file:
    input = (file.read()).strip()


##### Part 1 #####
def HasVowels(line):
    vowels = 'aeiou'
    vowel_count = 0
    for letter in line:
        if letter in vowels:
            vowel_count += 1
            if vowel_count == 3:
                return True

def HasDouble(line):
    for i in range(len(line[:-1])):
        if line[i] == line[i+1]:
            return True

def Contains(line):
    naughty_list = ['ab','cd','pq','xy']
    for badstring in naughty_list:
        if badstring in line:
            return True

##### Part 1 #####
def NiceLines(input):
    nice = 0
    for line in input.split():
        v = HasVowels(line)
        d = HasDouble(line)
        c = Contains(line)
        if v and d and not c:
            nice += 1
    return nice

part1 = NiceLines(input)
##### Part 2 #####

#part2 = 

if __name__ == '__main__':
    print("Day %s Part 1: %s" % (DAY, part1,))
    #print("Day %s Part 2: %s" % (DAY, part2,))
