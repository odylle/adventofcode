"""
Advent of Code 2015: Day 3
"""
# Get input
with open('input') as file:
    input = file.read()

def NewCoordinate(move, h, v):
    if move == '>':
        h += 1
    elif move == '<':
        h -= 1
    elif move == '^':
        v += 1
    elif move == 'v':
        v -= 1
    return h, v

##### Part 1 #####
def SaveCoordinates(input):
    coordinates = [(0, 0)]
    for move in input:
        h, v = coordinates[-1:][0]
        new = (NewCoordinate(move, h, v))
        coordinates.append(new)
    return coordinates

##### Part 2 #####
def SplitCoordinates(input):
    coordinates = [(0,0)]
    santa_location = robot_location = (0,0)
    for i in range(len(input)):
        if i % 2 == 0:
            h, v = santa_location
            new = (NewCoordinate(input[i], h, v))
            santa_location = new
        else:
            h, v = robot_location
            new = (NewCoordinate(input[i], h, v))
            robot_location =new
        coordinates.append(new)            
    return coordinates

if __name__ == '__main__':
    coordinates = SaveCoordinates(input)
    print("Day 3 Part 1: %i" % len(set(coordinates)))
    coordinates = SplitCoordinates(input)
    print("Day 2 Part 2: %i" % len(set(coordinates)))
