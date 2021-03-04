a=5
b=6
c="hello"
d="world"
print(a+b)
print(str.__add__(c,d)) #magic method
print(int.__add__(a,b))



class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,o):
        m1=self.m1+o.m1
        m2=self.m2+o.m2
        s3=student(m1,m2)
        return s3

s1=student(30,20)
s2=student(33,55)
s3=s1+s2
print(s3)