def fun(a,*nums):
    if len(nums) <= 0:
        print("incorrect")
    else:
        for i in nums:
            print(i)
            x= i**a

print(fun(2,5,6,7))





# (num   args    default num    kwargs )=========series of representing all if use all the var