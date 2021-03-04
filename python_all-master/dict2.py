user={}
user["name"]="parul"
user["age"]=20
print(user)
if 20 in user.values(): # if not write .values then default take keys
    print("yes it is in present ")
else:
    print("oops not present ")


for j in user.values():
    print("values",j)