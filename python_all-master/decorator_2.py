def square(a):
    return a**2
l=[1,2,3,4]
#print(list(map(square,l)))


def my_map(fun,l):
    new_list=[]
    for item in l:
        new_list.append(fun(item))
    return new_list
print(my_map(square,l))