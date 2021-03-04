x=55
def fun():
    x=100
    def fun2():
        global x              #for changing the value of global variable x 
        x=10
        print("hello the value of x  new is ",x)
    fun2()
    print("hello value of x old is ",x)
    
fun()
print(x)