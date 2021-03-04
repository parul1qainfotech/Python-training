from functools import wraps
import time
def decorator_time(any):
    @wraps(any)
    def wrap(*args,**kwargs):
        t1 = time.time()
        any(*args,**kwargs)
        t3 = time.time()
        t=t3-t1
    return wrap
@decorator_time

def timefun(z):
    print(f"the fun of time fun {z} secs ")
timefun(3)