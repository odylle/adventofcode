"""
Advent of Code 2015 
"""
DAY = 15

##### Functions #####
from itertools import product

class Cookies:

    def __init__(self):
        self.ingredients = {}
        self.properties = {}
        self.teaspoons = 0
        self.__import__()

    def __import__(self):
        with open ('input') as file:
            self.data = file.read().strip().split('\n')

    def _get_properties(self, p):
        property_ = ()
        for ingredient in self.ingredients:
            property_ = property_ + (self.ingredients[ingredient][p],)
        return property_

    def set_properties(self):
        options = ['capacity', 'durability', 'flavor', 'texture', 'calories']
        for option in options:
            self.properties[option] = self._get_properties(option)
        self.calories = self.properties.pop('calories')

    def process_import(self):
        for line in self.data:
            ingredient, properties = line.split(':')
            self.ingredients[ingredient] = {}
            properties = properties.split(', ')
            for p in properties:
                p = (p.strip()).split(' ')
                self.ingredients[ingredient][p[0]] = int(p[1])
        self.set_properties()

    def calculate_score(self, ratio, calories):
        score = 1
        negative = False
        for p in self.properties:
            ps = 0
            for pi in range(len(self.properties[p])):
                if calories != 0:
                    cals = sum(self.calories[i] * ratio[i] for i, cv in enumerate(self.calories))
                    if cals != calories:
                        return 0
                ps += ratio[pi] * self.properties[p][pi]
            if ps < 0:
                return 0
            score *= ps
        score = score if not negative else 0
        return score

def BestCooky(cal=0):
    high_score = 0
    maximum = cookies.teaspoons-(len(cookies.ingredients)-1)
    products = product(range(1, maximum+1), repeat=len(cookies.ingredients))
    for ratio in products:
        if sum(ratio) == cookies.teaspoons:
            score = cookies.calculate_score(ratio, calories=cal)
            high_score = max(score, high_score)
    return high_score

if __name__ == '__main__':
    cookies = Cookies()
    cookies.process_import()
    cookies.teaspoons = 100
    part1 = BestCooky()
    part2 = BestCooky(cal=500)

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
