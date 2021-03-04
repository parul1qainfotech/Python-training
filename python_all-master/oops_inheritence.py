#single inheritence
#multilevel inheritence
#multiple inheritence onle inherit two



class a:
    def feature(self):
        print("feature1")
    def feature2(self):
        print("feature 2")

class b(a):
    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature 4")


class c(b):
    def feature5(self):
        print("feature3")


class d(c,a):
    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature 4")
x=c()
x2=d()
x.feature4()
x2.feature()
x2.feature3()