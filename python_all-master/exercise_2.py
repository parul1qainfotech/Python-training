
'''def fun():
    x=[]
    for i in num:
        t=x.append(num[::])
        t.reverse()
        return t
print(fun())'''

num =["abc","xyz","mnp","rst"]
x = []
def fun():
    for m in num:
        for j in m[:1:1]:
            x.append(j)
    return(x)
print(fun())
