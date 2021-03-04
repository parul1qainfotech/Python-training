from functools import wraps

def decorator(x):
    @wraps(x)
    def wrap(*args,**kwargs):
        """hello wrap fun """
        print("hello")
        return x(*args,**kwargs)
    return wrap

@decorator
def add(a,b):
    """hello this is add function """
    return a+b



print(add(3,4))
