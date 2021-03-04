def num(n):
    for i in range(1,11):
        yield(i)

print(num(10))
for i in num(10):
    print(i)