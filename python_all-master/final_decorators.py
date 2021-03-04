# decorators = they are the function which enhance the functionality of the other fun

def decorator_fun(function):
    def wrapper_fun():
        print("this is additional line ")
        function()
    return wrapper_fun


@decorator_fun
# this is additional line
def fun1():
    print("this is fun1")
fun1()

@decorator_fun
# this is additional line
def fun2():
    print("this is fun2 ")


#var=decorator_fun(fun2)
#var()

