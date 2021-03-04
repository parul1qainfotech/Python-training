
# normal method
names=["abc","sajwan","parul","success"]
no=0
for i in names:
    print(f"{no} == {i}")
    no+=1

# using enumerator function

for no,i in enumerate(names):
    print(f"{no}=={i}")
