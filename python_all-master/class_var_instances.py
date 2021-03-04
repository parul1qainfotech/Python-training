# in this we are writing the value of pi again and again (take more memory )
class circle:
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    def cir(self):
        return 2*self.pi*self.radius
c=circle(4,3.14)
print(c.cir())


# it will take less memory and pi work as class instance
class circle:
    pi=3.14 # now this is the instance of class
    def __init__(self,radius):
        self.radius=radius
    def cir(self):
        return 2*circle.pi*self.radius
c1=circle(4)
print(c1.cir())
for i,j in (c.__dict__).items():
    print(f"key is {i} and value is {j}")
