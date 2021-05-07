class Campo:

    def __init__(self):
        self.coords = {}

    def add_drunk(self, drunk, coor):
        self.coords[drunk] = coor

    def move_drunk(self, drunk):
        dif_x, dif_y = drunk.walk()
        actual_coor = self.coords[drunk]
        new_coor = actual_coor.move(dif_x, dif_y)
        self.coords[drunk] = new_coor

    def move_funDrunk(self, drunk):
        dif_x, dif_y = drunk.otherWalk()
        actual_coor = self.coords[drunk]
        new_coor = actual_coor.move(dif_x, dif_y)
        self.coords[drunk] = new_coor

    def other_coord(self, drunk):
        return self.coords[drunk]