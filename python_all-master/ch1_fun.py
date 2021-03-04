a=int(input("enter the no"))
b=int(input("enter the no "))
s=a+b
print(s)


name,age="parul",20
print("hello"+ " "+name +""+"age is "+""+str(age))

# split method
name,age=input("enter the name and age ").split(",")
print(name)
print(age)


# string formatting
#python 3
print("{} your name is {}".format(age,name)) #{} are place holder
#python 3.6
print( f"hello your name is {name} and age is {int(age)+2} after two year ")

