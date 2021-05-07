class Coordenada:

    def __init__(self,x,y):
        self.x, self.y = x, y

    def move(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def dist(self, other_coor):
        dif_x = self.x - other_coor.x
        dif_y = self.y - other_coor.y
        return(dif_x**2 + dif_y**2)**.5