"""
Advent of Code 2015: Day 6 
"""
DAY = 6

# Get input
with open('input') as file:
    input = (file.read()).strip()

##### Helpers #####
class Lights():
    def __init__(self):
        self.lights = {}
        self.new_lights()
        self.get_input()
    
    def new_lights(self):
        xr = yr = range(0, 1000)
        for x in xr:
            for y in yr:
                self.lights[(x, y)] = 0

    def get_input(self):
        with open('input') as file:
            self.input = (file.read()).strip()

    def _setState(self, light, action):
        if self.lights[light] == 0:
            if action == 'toggle' or action == 'on':
                self.lights[light] = 1
        else:
            if action == 'toggle' or action == 'off':
                self.lights[light] = 0
    
    def _setBrightness(self, light, action):
        if action == 'toggle':
            self.lights[light] += 2
        if action == 'on':
            self.lights[light] += 1
        if action == 'off':
            if self.lights[light] > 0:
                self.lights[light] -= 1

    def _processInstructions(self):
        for line in (self.input).split('\n'):
            line = line.split()
            action, sr, er = line[-4], line[-3], line[-1]
            xs, ys = map(int, sr.split(','))
            xe, ye = map(int, er.split(','))
            for x in range(xs, (xe+1)):
                for y in range(ys, (ye+1)):
                    self._setState((x, y), action)

    def _processElvishInstructions(self):
        for line in (self.input).split('\n'):
            line = line.split()
            action, sr, er = line[-4], line[-3], line[-1]
            xs, ys = map(int, sr.split(','))
            xe, ye = map(int, er.split(','))
            for x in range(xs, (xe+1)):
                for y in range(ys, (ye+1)):
                    self._setBrightness((x, y), action)

    def litCount(self):
        self._processInstructions()
        self.lit = 0
        for light in self.lights:
            if self.lights[light] == 1:
                self.lit += 1
    
    def totalBrightness(self):
        self._processElvishInstructions()
        self.brightness = 0
        for light in self.lights:
            self.brightness = self.brightness + self.lights[light]


if __name__ == '__main__':
    lights = Lights()
    lights.litCount()
    part1 = lights.lit

    ##### Part 2 #####
    brightlights = Lights()
    brightlights.totalBrightness()
    part2 = brightlights.brightness

    print("Day %s Part 1: %s" % (DAY, part1,))
    print("Day %s Part 2: %s" % (DAY, part2,))
    
