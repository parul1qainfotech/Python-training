#noraml method
s=[]
for i in range(1,11):
    s.append(i**2)
print(s)

#list comrehension - shorten the code
s2=[i**2 for i in range (1,11)]
print("list comprehension",s2)


s3=[-i for i in range(1,11)]
print(s3)