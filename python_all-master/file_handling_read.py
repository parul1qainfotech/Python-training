f=open("parul.txt","rt")
# content=f.read(131111)
# print(content)
# content=f.read(31111111)
# print(content)

# f.close()



    
#different methods for line by line reading
#for line by line
for i in f:
    print(i,end="")
#readline
print(f.readline())
print(f.readline())
print(f.readline())

#readlines-convert the lines to list 
print(f.readlines())



#seek and tell in file
# tell= tell the postion pointer of File 
# seek= repointer the point 
# seek(10)- return to 10 position