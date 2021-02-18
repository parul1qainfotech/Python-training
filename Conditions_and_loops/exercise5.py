#Write a loop to find the factorial of any number
res=1
fact=int(input("enter the number for factorial"))
if(fact==0):
    res=0;
elif(fact<0):
    print("factorial of negative number cannot be find")

else:
    for i in range(1,fact+1):
        res=res*i
print("Factorial of %d is" %(fact),res)
        