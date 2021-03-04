# split- it split the string into list
# if want to split the integer then convert it into the str first

user_info="parul_sajwan"
user=str(1234)
print(type(user))
print(user_info.split("_"))
x=user.split()

m=['hello','parul']
t=",".join(m)
print(type(t))
print("t",t)

num= list(range(1,11))
print(num)
#index in list
print(num.index(3))
print("index",num.index(1)) #      index no    start from    end at

def fun():
    no=[]
    for i in range (0,10):
        no.append(i)
    return no
print(fun())

#reverse
p=[2,3,4,5,342,2]
print("_________________________________________")
print(sorted(p,reverse=True))
print(p.reverse())  # it doesnt return anything
print(p)