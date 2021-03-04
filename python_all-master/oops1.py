#object oriented programming

class Person: # first letter is captial, its a convention not necesssary.
    def __init__(self,first_name,last_name,age): #init is constructor
        self.first=first_name
        self.last=last_name
        self.age=age


p1=Person("parul","sajwan",20)
p2=Person("simran","sajwan",21)

print(p1.first)
print(p2.first)
print(p1)
