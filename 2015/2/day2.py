"""
Advent of Code 2015: Day 2
"""

from input import input

def PackageList(input):
    packages = []
    for row in input.split():
        packages.append(list(map(int, row.split('x'))))
    return packages

##### Part 1 #####
def totalWrappingPaper(packages):
    total = 0
    for package in packages:
        l, w, h = package
        volume = (2*l*w)+(2*w*h)+(2*h*l)
        overhead = (sorted(package)[0]*sorted(package)[1])
        total += volume+overhead
    return total

##### Part 2 #####
def getRibbon(packages):
    total = 0
    for package in packages:
        l, w, h = package
        around = (sorted(package)[0]*2)+(sorted(package)[1]*2)
        bow = l*w*h
        total += around+bow
    return total

if __name__ == '__main__':
    packages = PackageList(input)
    print("Day 2 Part 1: %i" % totalWrappingPaper(packages))
    print("Day 2 Part 2: %i" % getRibbon(packages))
