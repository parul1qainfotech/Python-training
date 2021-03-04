#default argument
'''def user_info(f,l='unknown',a=None):# we can make only the last argument as default
    print(f"user name {f} and last name is {l} and age is {a}")

user_info('parul','sajwan')
'''




# scope of variable
x=5
def fun():
    global x  # if want to use the global inside the fun
    x=3  #local value
    return x
print("global",x)
print("local",fun())
print("global",x) # now value is replaced because we are using it inside the function as global var