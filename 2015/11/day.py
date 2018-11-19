"""
Advent of Code 2015 
"""
DAY = 11 

##### Functions #####
import string
class PasswordRequirements:

    def __init__(self):
        self.length = 8
        self.charset = string.ascii_lowercase
        self.index = 0
        self.excluded = ['i', 'o', 'l']
        self.allowed_chars = self.__allowed_chars()
        self.straights = self.__list_straights()

    def has_forbidden(self, s):
        for char in self.excluded:
            if char in s:
                return True

    def __list_straights(self):
        straights = []
        i = 0
        while i < len(self.charset):
            if i+3 == len(self.charset):
                if not self.has_forbidden(self.charset[i:i+3]):
                    straights.append(self.charset[i:i+3])
                    break
            else:
                if not self.has_forbidden(self.charset[i:i+3]):
                    straights.append(self.charset[i:i+3])            
            i += 1
        return straights

    def has_straight(self, s):
        for straight in self.straights:
            if straight in s:
                return True

    def has_pairs(self, s):
        pairs = i = 0
        while i < len(s[:-1]):
            if s[i] == s[i+1]:
                # Pair Found!
                if i+1 <= len(s):
                    pairs += 1
                i += 1
            i += 1
        if pairs >= 2:
            return True

    def __allowed_chars(self):
        allowed_chars = ''
        i = 0
        while i < len(self.charset):
            if not self.has_forbidden(self.charset[i]):
                allowed_chars = allowed_chars+self.charset[i]
            i += 1
        return allowed_chars

def FindNewPassword(current):
    pwd = list(current)[::-1]
    while True:
        for i in range(len(pwd)):
            pwd[i] = chr(ord(pwd[i])+1) if pwd[i] != 'z' else chr(ord('a'))
            new = ''.join(pwd)        
            if pwd[i] != 'a':
                break
        if (req.has_pairs(new[::-1]) and 
                req.has_straight(new[::-1]) and 
                not req.has_forbidden(new[::-1])):
            break
    return new[::-1]

if __name__ == '__main__':
    req = PasswordRequirements()
    current = 'hxbxwxba'
    new = FindNewPassword(current)
    part1 = new
    part2 = FindNewPassword(new)

    if part1:
        print("Day %s Part 1: %s" % (DAY, part1,))
    if part2:
        print("Day %s Part 2: %s" % (DAY, part2,))
    
