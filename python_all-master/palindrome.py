def fun(a):
    b=a[::-1]
    if a==b:
        return (f" {a} is palindrome ")
    return (f" {a} is not a plaindrome ")
no=input("enter the name:")
print(fun(no))