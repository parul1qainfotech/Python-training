#tuples: they are immutable
#tuples are faster then list

num=(1,2,4,44,2)
print(num)

#tuple unpacking
x1,x2,x3,x4,x5=(num)
print(x3)


#list inside the tuple an be change

name=(1,2,3,[3,31,3,1],"a","x")
print(name[3].pop())
print(name[3])