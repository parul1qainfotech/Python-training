
#noraml function
def fun(a):
    if a%2==0:
        return True
    else:
        return False
print(fun(3))

# lambda function
fun2=lambda a: a%2==0
print(fun2(32))




#lambda with if else
def fun(s):
    if len(s)>2:
        return True
    else:
        return False

print(fun('hello'))

#same prog using lambda
w=lambda s:True if len(s)>3 else False
print(w("parul"))