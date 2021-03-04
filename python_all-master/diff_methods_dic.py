my_info={"first_name":"parul","last_name":"sajwan","age":20}
print(my_info.items())
print(type(my_info.items()))

# pop method
print(my_info.pop("first_name"))
print(my_info)
#print(my_info["first_name"])    now show the error
print(my_info.popitem())  # key value deleted pair will show


# update method in dictionary
frnd_info={"first_name":"rajat","last_name":"bhalla","age":21}
my_info={"first_name":"parul","last_name":"sajwan","age":20}

my_info.update(frnd_info) # values are updated or changed by myinfo to frnd info
print(my_info)
my_info.update({})
print(my_info)


#from keys
d=dict.fromkeys("string",'unknown')
print(d)
dd=dict.fromkeys(("a","b","a","d"),"hello")
print(dd)
cc=dict.fromkeys((1,2,3,"s"),"hello")
print(cc)
ddd=dict.fromkeys([1,23,"parul"],34)
print(ddd)
ddd=dict.fromkeys(range(0,19),"numbers")
print(ddd)


#get method
print(my_info.get("name",{"hey":"hello"})) #if the key is not present then doesnt give error it  shows none and we can give default para also
print(my_info.get("last_name","let me check")) # here let me chk is default if last_name cannt be find
print(my_info.get(20,"default parameter hai bhai bczz key to hai ni "))

#copy method
d1={"1":2,"1":3} # if the dict contain the more same key then the value of second key will replace by first one
d2=d1.copy() # it copy the content to different variable
print(d2)
d1.pop("1")
print(d1)
print(d2)
