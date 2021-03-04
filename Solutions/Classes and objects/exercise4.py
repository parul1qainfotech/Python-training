#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        print(f"Area is {3.14*self.radius**2}")
    
    def perimeter(self):
        print(f"Perimeter is {2*3.14*self.radius}")
        
    
c1=Circle(8)
c1.area()
c1.perimeter()
