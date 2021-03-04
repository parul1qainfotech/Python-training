def fun(n):
    n = int(input("enter the no"))
    for i in range(0,n):
        if n%2==0:
            yield (n)

for i in fun(20):
    print(i)