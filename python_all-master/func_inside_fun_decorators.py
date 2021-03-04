# function inside func /fun returning fun

def outer_fun():
    def inner_fun():
        print("this is inner fun ")
    return inner_fun

x=outer_fun()
x()


def o(a):
    def i():
        print(f"hello{a}")

    return i
z=o("parul")
z()