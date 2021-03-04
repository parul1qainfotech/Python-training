#Accept number from user and calculate the sum of all number between 1 and given number.
sum=0
number=int(input("enter the number"))
for i in range(1,number+1):
    sum=sum+i
print("sum of number is:", sum)