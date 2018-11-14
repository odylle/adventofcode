"""
Advent of Code 2015 
"""
DAY = 9 

from collections import defaultdict
from itertools import permutations

class Paths():

    def __init__(self):
        self.locations = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def _add_node(self, value):
        self.locations.add(value)

    def _add_edge(self, from_location, to_location, distance):
        self.edges[from_location].append(to_location)
        self.edges[to_location].append(from_location)
        self.distances[(from_location, to_location)] = int(distance)

    def process_input(self):
        with open('input') as file:
            f = file.read().strip().split('\n')
        for i in range(len(f)):
            l1, _, l2, _, distance = f[i].split()
            for l in (l1, l2):
                self._add_node(l)
            self._add_edge(l1, l2, distance)
    
    def get_distance(self, l1, l2):
        for path in self.distances:
            if l1 in path and l2 in path:
                return self.distances[path]

    def shortest(self):
        paths = permutations(list(self.locations))
        self.best_distance = 100000
        self.best_path = None
        for path in list(paths):
            distance = 0
            for i in range(len(path[:-1])):
                distance += self.get_distance(path[i], path[i+1])
                if distance < self.best_distance:
                    if i == 6: # Last iterations, means full route
                        self.best_distance = distance
                        self.best_path = path
                else:
                    break
        return self.best_distance

    def longest(self):
        paths = permutations(list(self.locations))
        self.worst_distance = 0
        self.worst_path = None
        for path in list(paths):
            distance = 0
            for i in range(len(path[:-1])):
                distance += self.get_distance(path[i], path[i+1])
                if i == 6:
                    if distance > self.worst_distance:
                        self.worst_distance = distance
                        self.worst_path = path
        return self.worst_distance     



if __name__ == '__main__':
    p = Paths()
    p.process_input()
    part1 = p.shortest() 
    part2 = p.longest()

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
