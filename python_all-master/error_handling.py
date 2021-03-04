a=4
b=0

try:
    print(a/b)


except ZeroDivisionError as e:
    print("you are dividing by 0",e)

except ValueError as e:
    print("this is a value error ",e)

except Exception as e:
    print("you have an error ",e)

finally:
    print("this will definitely run ")