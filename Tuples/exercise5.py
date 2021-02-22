#Remove duplicate from a list and create a tuple and find the min and max number.

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

uniqueItems=[]
for i in sampleList:
    if i not in uniqueItems:
        uniqueItems.append(i)

print("Unique Items:",uniqueItems)
print("tuple:",tuple(uniqueItems))
print("mininum:" ,min(uniqueItems))
print("mininum:" ,max(uniqueItems))