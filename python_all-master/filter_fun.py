#filter fun : it takes the arguments as fun and sequence of list or iterators and return the result in the another object or var ,thte result return will be true result only which follow the condition
#map fun: map fun also take two arg fun or iterators it follow the list and solve the function and give the result

n=[1,2,3,4,5]
#without lambda
'''def fun(a):
    if a>2:
        return a'''

#with lambda fun
x=list(filter (lambda a: a>2 ,n))
y=list(map (lambda a: a>2 ,n))
print(x)
print(y)

