"""
Advent of Code 2015 
"""
DAY = 14 

##### Functions #####
class Reindeer:

    def __init__(self):
        self.reindeer = {}
        self.__import__()

    def __import__(self):
        with open('input') as file:
            self.data = file.read().strip()
            self.data = self.data.split('\n')

    def process_import(self):
        for line in self.data:
            l = line.split(' ')
            name, speed, time, rest = l[0], l[3], l[6], l[-2]
            self.reindeer[name] = { 
                'speed': int(speed), 
                'time': int(time), 
                'rest': int(rest),
                'points': 0 }

    def furthest(self, seconds):
        furthest = 0
        for name in self.reindeer:
            distance = self.distance_after(name, seconds)
            if distance > furthest:
                furthest = distance
        return int(furthest)

    def distance_after(self, name, seconds):
        remain = seconds % (self.reindeer[name]['time']+self.reindeer[name]['rest'])
        multiplier = (seconds-remain)/(self.reindeer[name]['time']+self.reindeer[name]['rest'])
        distance = (self.reindeer[name]['speed']*self.reindeer[name]['time'])*multiplier
        if self.reindeer[name]['time'] < remain:
            distance += self.reindeer[name]['speed']*self.reindeer[name]['time']
        else:
            distance += self.reindeer[name]['speed']*remain
        return int(distance)

    def points_after(self, seconds):
        for second in range(seconds+1):
            if second > 0:
                how_far = []
                furthest_distance = 0
                for name in self.reindeer:
                    distance = self.distance_after(name, second)
                    if distance > furthest_distance:
                        furthest_distance = distance
                    how_far.append((name, distance))
                for check in how_far:
                    if furthest_distance in check:
                        self.reindeer[check[0]]['points'] += 1

    def most_points(self):
        most = 0
        for name in self.reindeer:
            if self.reindeer[name]['points'] > most:
                most = self.reindeer[name]['points']
        return most

if __name__ == '__main__':
    reindeer = Reindeer()
    reindeer.process_import()
    part1 = reindeer.furthest(2503)
    reindeer.points_after(2503)
    part2 = reindeer.most_points()

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
