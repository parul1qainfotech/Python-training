l1=[1,2,3,4]
l2=[2,3,4,1]
x=list(zip(l1,l2))
print(x)


m=[(1, 2), (2, 3), (3, 4), (4, 1)]
l3,l4=zip(*m)
print(list(l3))
print(list(l4))




n=[]
for i in list(zip(l1,l2)):
    n.append(max(i))
print(n)


