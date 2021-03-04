'''def fun(a,b):
    print (a+b)

x= int(input("enter the value of x :"))
y= int(input("enter the value of  y:"))'''


# return the last char of the name
def fun(a):
    return a[-1]
x=input("enter the name:")
print(fun(x))




# return odd or even
'''def fun(a):
    if a%2==0:
      print("even")
    else:
      print ("odd")
x=int(input("enter the number :"))
fun(x)
'''
def fun(a):#parameter
    if a%2==0:
      return("even")
    return ("odd")
x=int(input("enter the number :"))
print(fun(x))#argument