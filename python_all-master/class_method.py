# accessor : if use the   value or cannt to chng the value (get or getter ) ,
# and mutator : if use the modified value or change the value (set or setter )
# methods :
''' 1. instamce method : the method whicha pass the self arg
2. class method : which pass the class
3.static method '''
class fun:
    xx=6 #class var
    def __init__(self,x):
        fun.xx
        self.x=x
    def nice(self):
        return (f"hello {self.x}")

    @classmethod
    def count(cls):
        return (f"this is class instance  :{cls.xx} and the instance method is ")

print(fun.count())
p1=fun(3)
print(f"hello  {p1.x}")
