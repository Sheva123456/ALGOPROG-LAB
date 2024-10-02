class circle:
    def __init__(self, radius = 13, color = 'pink', pi = 3.14):
        self.radius = radius 
        self.color = color 
        self.pi = pi
    def getColor(self):
        print(self.color)
    def getCircum(self):
        print(2*self.pi*self.radius)

yo = circle()
yo.getColor()
yo.getCircum()