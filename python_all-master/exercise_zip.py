
l3=[]
def fun(*l):
    arg=list(zip(*l))
    print(arg)
    for j in arg:
        for i in j:
            l3.append(i)
    return tuple(set(l3))

print(fun([12,2,3],[3,3,3,4],[5,6,3],[3,3,2]))


