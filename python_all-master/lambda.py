# it is also called anonymous

# lambda fun is a fun which dont have any name and define in a line
#lambda is used with builtin functions not assign with var

def add1(a,b):
    return a+b
print(add1(3,2))
add2=lambda a,b: a+b
print(add2(3,4))

print(add1)
print(add2)



new =lambda a,b : print( "hello %s your friend is %s" %(a,b))

new("parul","simran")