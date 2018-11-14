"""
Advent of Code 2015 
"""
DAY = 7

class Wires():

    def __init__(self):
        self.wires = {}
        self._get_input()

    def _get_input(self):
        with open('input') as file:
            self.instruction_set = (file.read()).strip()
            self.instruction_set = sorted(self.instruction_set.split('\n'))

    def _replace(self, operator):
        """
        _replaces operator with python compatable operator
        """
        if operator == 'AND':
            operator = '&'
        elif operator == 'OR':
            operator = '|'
        elif operator == 'RSHIFT':
            operator = '>>'
        elif operator == 'LSHIFT':
            operator = '<<'
        elif operator == 'NOT':
            operator = '~'
        return operator

    def _isWire(self, wire):
        if wire in self.wires:
            return str(self.wires[wire])
        return wire        

    def solve(self):
        while len(self.instruction_set) > 0:
            for instructions in self.instruction_set:
                instruction, wire = instructions.split('-> ')
                instruction = instruction.split()
                if len(instruction) == 1:
                    l = self._isWire(instruction[0])
                    if l.lstrip('-').isdigit():
                        if wire not in self.wires:
                            self.wires[wire] = l
                        self.instruction_set.remove(instructions)
                elif len(instruction) == 2:
                    operator = self._replace(instruction[0])
                    if instruction[1] in self.wires:
                        r = self._isWire(instruction[1])
                        if r.lstrip('-').isdigit():
                            self.wires[wire] = eval(operator+r)
                            self.instruction_set.remove(instructions)
                elif len(instruction) == 3:
                    operator = self._replace(instruction[1])
                    l = self._isWire(instruction[0])
                    r = self._isWire(instruction[2])
                    if l.lstrip('-').isdigit() and r.lstrip('-').isdigit():
                         self.wires[wire] = eval(l+operator+r)
                         self.instruction_set.remove(instructions)

if __name__ == '__main__':
    p1 = Wires()
    p1.solve()
    part1 = p1.wires['a']

    p2 = Wires()
    p2.wires['b'] = p1.wires['a']
    p2.solve()
    part2 = p2.wires['a']

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
