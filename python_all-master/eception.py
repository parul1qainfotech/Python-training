a=input("enter the first number")
b=input("enter the 2nd number")
def function1(a,b):
    try:
        print("the sum of the two number is ",int(a)+int(b))
    except Exception as e:
        print("error:",e)
function1(a,b) 


    