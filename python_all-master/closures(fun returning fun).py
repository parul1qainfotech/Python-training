def power(a):
    def value(b):
        return b**a
    return value
n=power(2)
print(n(2))