"""
Advent of Code 2015 
"""
DAY = 18 

##### Functions #####
# Spawn 100x100 blank grid
grid = {}
for x in range(100):
    for y in range(100):
        grid[(x, y)] = 0

# Get: grid initial state from input
with open('input') as file:
    f = file.read().strip()

# Set: grid initial state
rows = f.split('\n')
for x in range(len(rows)):
    for y in range(len(rows[x])):
        if rows[x][y] == '#':
            grid[(x, y)] = 1

# Class for easy assignments
class Lights:
    pass

def GetNeighbors(light):
    """
    Returns all the neighbors for our light
    """
    neighbors = []
    x, y = light
    for xi in range(x-1, x+1+1):
        for yi in range(y-1, y+1+1):
            if xi in range(0, 100) and yi in range(0,100):
                if xi != x or yi != y:
                    neighbors.append((xi, yi))
    return neighbors

def GetNeighborsOn(neighbors):
    """
    Return total number of neighbors in 'on' state
    """
    on = 0
    for n in neighbors:
        if lights.grid[n] == 1:
            on += 1
    return on

def SetState(broken=None):
    """
    Set new state and update grid.
    'broken' accepts a list of broken lights that are 'on'.
    """
    newgrid = dict(lights.grid)
    for light in lights.grid:
        neighbors = GetNeighbors(light)
        on = GetNeighborsOn(neighbors)
        if lights.grid[light] == 1:
            newgrid[light] = 1 if on == 2 or on == 3 else 0
        else:
            newgrid[light] = 1 if on == 3 else 0
        if broken:
            if light in ((0, 0), (0, 99), (99, 0), (99, 99)):
                newgrid[light] = 1            
    lights.grid = dict(newgrid)

def GetOnLights():
    """
    Count a'l the lights that are 'on' (1)
    """
    on = 0
    for light in lights.grid:
        if lights.grid[light] == 1:
            on += 1
    return on 


if __name__ == '__main__':
    steps = 100

    # Part 1
    lights = Lights()
    lights.grid = dict(grid)

    i = 0
    while i < 100:
        SetState()
        i += 1

    part1 = GetOnLights()

    # Part 2
    lights = Lights()
    lights.grid = dict(grid)

    i = 0
    while i < 100:
        SetState(broken=((0, 0), (0, 99), (99, 0), (99, 99)))
        i += 1

    part2 = GetOnLights()

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
