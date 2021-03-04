i=[1,2,3,4,5,6,7,8,9,10]
s=[i for i in i if i%2==0]
print("even",s)


#if_else

num=[1,2,3,4,5,6,7,8,9,10]
value=[i**2 if (i%2==0) else (-i) for i in num]
print(value)