num=int(input("enter the number"))
boolen=str(bool(input("enter true or false")))
print(type(boolen))


for i in range(num+1):
    for j in range(i):
        print("*",end="")
    print("\n")

        

