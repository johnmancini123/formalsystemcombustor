#s is a string representing the word.
#n is a numer representing which decision was made to get there
class node:
    def __init__(self, val, rule, parent):
        self.val = val
        self.rule = rule
        self.parent = parent
    def __str__(self):
        return "[" + self.val + ", " + str(self.rule) + ", " + str(self.parent) + "]"

