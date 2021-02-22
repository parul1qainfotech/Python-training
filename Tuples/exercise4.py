#Swap the following two tuples

tuple1 = (11, 22)
tuple2 = (99, 88)

def fun1(tuple1,tuple2):
    tuple1,tuple2=tuple2,tuple1
    return tuple1,tuple2

print(fun1(tuple1,tuple2))

