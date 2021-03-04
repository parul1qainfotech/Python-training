fruits1=["apple","mango","orange","banana","cheery"]
fruits2=["apple","orange","banana","cheery","apple"]
a=[]
b=[]
c=b
print( fruits1==fruits2 ) # it check whether the value are equal or not
print(fruits1 is fruits2)
print(b is b)
print(b is c)# if both have same id(assignment)