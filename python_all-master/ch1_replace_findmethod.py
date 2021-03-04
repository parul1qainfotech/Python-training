name="she is a girl  and she is good dancer "
print(name.replace("is","was",1)) # 1 denotes replace the first is
print(name.find("i",5)) # find from 5 position

name2="she is a girl  and she is good dancer "
is_pos1=name.find("is")
is_pos2=name.find("is",is_pos1+1) # +1 because it will start from next place to  first is

# center method
a="simran"
b=len(a)
print(a.center(b+12,"*"))
