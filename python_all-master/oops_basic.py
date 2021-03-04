# for a class there are two things are imp
'''1.attribute-variable
2. behaviour-method(fun)'''




''' in this we have two special 
1.special method - __main__
2.__init___  = this is mainly for the intialization and work as constructor '''

""" variables 
1.instancee variable : inside init
2.class var : inside class outside init """

class main:

    def __init__(self,x):
        self.x=x


    def config(self):
        print(f"hello {self.x}")

com1=main("parul")
com2=main(5)
main.config(com1)
main.config(com2) # this shows basically the working of the working

com1.config() # most of the time we use this

    

