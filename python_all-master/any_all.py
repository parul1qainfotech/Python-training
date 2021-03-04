number1=[1,2,35,4,6,7]
number2=[4,5,6,72,1,3,4]
e=[]
for i in  number1:
    e.append(i%2==0)   # if the given condition is true and false  (here the print true if satisfy)
print(e)




#all function
print(all([False, True, False, True, True, False])) #if any one will be false then result will be false  ,it satisfy the condition when all is true

#any function
print(any([False, True, False, True, True, False])) # in this if any of one is true then the result will be true
