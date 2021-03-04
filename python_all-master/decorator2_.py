from functools import wraps   # if we dont import the functools then it will return the wrapper fun doc string

def decorator_fun(anyfun):
    @wraps(anyfun)
    def wrapper_fun(*args,**kwargs):
        """ hello  wrapper doc string """
        print(f"this is fun")
        return anyfun(*args,**kwargs)
    return wrapper_fun

@decorator_fun
def fun1(a):
    """ hello fun doc string """
    print(f"the no is {a}")
fun1(4)
print(fun1.__doc__)
print(decorator_fun.__doc__)#it does print anythong for that we have to import the fun
print(fun1.__name__)