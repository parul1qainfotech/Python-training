#list are mutable

num=[0,1,1,'a']
print(num)
print(num[1])
print(num[:-3])
print(type(num))
num[1]="parul" #mutable
print(num)
num.append("toffee") # append at the last only
num.insert(1,'sajwan') # insert at that postion
a=[1,2,3]
b=[3,4,5]
c=a+b
print("not assigned ",a+b)
a.extend(b) # the b will be added to dthe list of a
print("assigned",c)
print("extend",a)
print("before popping:",num) # pop element delete by giving the index and return the va;ue also
print("popped element:",num.pop(2))# by default it  delete the last when no arg is given  ohterwise the indexed no
print("after popoing:",num)
#print("delete",del num[1])# deleted element cannt be return
del num[1]
print("after deleting:",num)
print("after remove",num.remove("a")) # remove cannt remove the value
print("after removing:",num)
