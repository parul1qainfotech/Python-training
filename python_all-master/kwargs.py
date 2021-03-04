#kwargs(keyword argument)========== it return the dictionary

def fun(**kwargs):
    return kwargs
print(fun(name='parul',age=20))


d={"name":"parul","last_name":"sajwan","age":20}
print(**d)