#iterartors and iterables
num=[1,2,3,4,5]#iterable
x=map(lambda a: a in num , num)
for i in num:
    print(i)


    # iter()
    #iter(num)===iterator
    #next(iter(num))=====print each iterator

print(next(iter(num))) # iterables
print(next(x))         #iterator