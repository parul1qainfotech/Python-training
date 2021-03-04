l=[True,False,[1,2,3],1,1.0,3]
s=[str(i) for i in l if type(i)==int or type(i)==list or type(i)==float]
print(s)
