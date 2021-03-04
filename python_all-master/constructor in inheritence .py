# child class which inherit the features from paresnt class or super class
''' in multiple inheritence if
1.if the child and super class have same method it will firstly call the object class and then if not in hcild then chk for super
2.but if we want to call the super class first then we use the supeer method

        3.                       a           b
                                     c

here c is the child class of a and b and a &b are the super classes then if the all have the same function then which one super class fun will call first


so this will be done by  method resolution order (mro) that means left super class will run first '''



class a:
    def __init__(self):
        print("super class of b")
    def my(self):
        print("i am from class a")

class b:
    def __init__(self):
        print("child class b")

    def my(self):
        print("i am from class b")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("it is multiple inheritence c class ,child class of a and b")

x=c()
x.__init__
x.my()