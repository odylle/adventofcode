"""
Advent of Code 2015 
"""
DAY = 13 

##### Functions #####
from itertools import permutations

class Seating:

    def __init__(self):
        self.attendees = set()
        self.happiness = {}
        self.__import__()

    def __import__(self):
        with open('input') as file:
            self.data = file.read().strip()
            self.data = self.data.split('\n')

    def process_import(self):
        for line in self.data:
            l = line.split(' ')
            #attendee, change, value, neigbour
            a, c, v, n = l[0], l[2], l[3], l[10]
            self.attendees.add(a)
            c = '+' if c == 'gain' else '-'
            self.happiness[(a, n[:-1])] = int(c+str(v))

    def combine_happiness(self):
        self.combined = {}
        for n in self.happiness:
            a, b = n
            if (not (a, b) in self.combined
                and not (b, a) in self.combined):
                self.combined[(a, b)] = self.happiness[n]
            if ((b, a) in self.combined):
                self.combined[(b, a)] += self.happiness[n]

    def get_happiness(self, neighbours):
        a, b = neighbours
        if (a,b) in self.combined:
            return self.combined[(a, b)]
        else:
            return self.combined[(b, a)]

    def optimal_seating(self):
        p = permutations(self.attendees)
        optimal = 0
        for order in list(p):
            happiness = 0
            for i in range(len(order)):
                if i+1 == len(order):
                    neighbours = (order[i], order[0])
                else:
                    neighbours = (order[i], order[i+1])
                happiness += self.get_happiness(neighbours)
            if happiness > optimal:
                optimal = happiness
        return optimal

if __name__ == '__main__':
    seating = Seating()
    seating.process_import()
    seating.combine_happiness()
    part1 = seating.optimal_seating()

    # Add Me
    for attendee in seating.attendees:
        seating.happiness[('Me', attendee)] = 0
    seating.attendees.add('Me')
    seating.combine_happiness()
    part2 = seating.optimal_seating()

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
