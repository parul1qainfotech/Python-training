'''def total(a,b):
    return a+b
print(total(2,2,2))
'''

#* args take multiple arg     ====== it return the tuple
def total(*args):
    x=0
    for i in args:
        x+=i
        print(x)
total(3,3,3,3,3)


def fun(num,*args): # single var always define first before args
    total=0
    for i in args:
        total+=i
        s=num+total
        return s
print(fun(2,33))