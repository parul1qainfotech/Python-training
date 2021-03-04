class student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.laptop=self.laptop


    def show(self):
        print(f"hello {self.name}")


    class laptop:

        def __init__(self):
            self.brand="hp"
            self.price="50000"

s=student("parul",20)
student.show(s)

sl=student.laptop()
print(sl.brand)
print(sl.price)
