class Line(object):
    def __init__(self, coord1, coord2):
        self.coor1 = coord1
        self.coor2 = coord2

    def distance(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return ((x2-x1)**2 + (y2-1)**2)**0.5

    def slope(self):
        x1, x2 = self.coor1
        y1, y2 = self.coor2
        return (x2-x1)/(y2-y1)


coor1 = (3,8)
coor2=(4,10)
line=Line(coor1, coor2)
#print(line.distance())
#print(line.slope())

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * (3.14 * (self.radius)**2)

    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)

cylinder = Cylinder(2,3)
print(cylinder.volume())
print("some sexy surface area action: ", cylinder.surface_area())
