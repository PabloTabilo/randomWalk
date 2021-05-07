import random

class Borracho:

    def __init__(self, name):
        self.name=name

class BorrachoTradicional(Borracho):

    def __init__(self, name):
        super().__init__(name)

    # (x,y)
    def walk(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

    def otherWalk(self):
        pos_x = 1 if random.random()<=.5 else 0
        pos_y = 1 if random.random()<=.5 else 0
        pos_x = -1 if random.random()<=.5 else pos_x
        pos_y = -1 if random.random()<=.5 else pos_y
        return (pos_x, pos_y)