#Write a function func1() such that it can accept a variable length of  argument and print all arguments value.


def func1(*args):
    print(*args)
    
func1(20,40,60)
func1(80,100)