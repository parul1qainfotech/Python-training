# dic is the key value pair ana can be mutable
# they are unordered collection there is no indexing available


# different ways to represent the dictionary
user={"name":"parul","surname":"sajwan","age":20}
print(user["name"])
print(user["age"])
print(user)

user1=dict(name="simran",age=20)
print(user1)

user2={
    'name':"parul",
    'age':20,
    "course":"btech",
    "subject marks":[100,93,98,97],
    "user3":{

        "name":"kyun btau",
        "age":"galt baat mat puch "
    }

}
user2["user3"]["height"]="sabse lambi"
print("height:",user2["user3"]["height"])

print(user2["course"])
print("age:",user2["user3"]["name"])
print("________________________________________")
print("items ",user2.items()) #key value pair in form of tuple
