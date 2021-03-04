num1=[2,3,1,4]
num2=[1,4,5,7,8]
x=[]
for i in num2:
    if i in num1:
        x.append(i)
print(x)


nums=[2,3,4,5,1,5,10]
print(min(nums))
print(max(nums))
print("______________________________________")

s=[1,2,3,[2,1,2],[2,2,2]]
no=0
for i in s:
    if type(i) == list :
        no=no+1

print(no)