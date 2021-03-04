#map function
num=[1,2,3,4]
def sq(a):
    for i in num:
        a= i**2
        print(a)
print(sq(num))



#map function with lambda                              map(functions,iterations)
sq=list(map(lambda a:a**2,num))
print(sq)
# map function is iterable
m=["a","abc","ab"]
leng=map(len,m)
print(leng)
for i in leng:
    print(i)