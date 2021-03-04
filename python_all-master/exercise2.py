# for counting the no of char in your name
name=input("enter your name ")
i=0

j=name
temp=""
for i in range (len(name)):
    if name[i] not in temp:
        temp+= name[i]

        t=name.count(temp)
        print(f"no {name[i]} occur {t} times ")


