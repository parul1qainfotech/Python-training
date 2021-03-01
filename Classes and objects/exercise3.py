#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def Area(self):
        print(self.length*self.width)
        
area=Rectangle(12,10)
area.Area()

    