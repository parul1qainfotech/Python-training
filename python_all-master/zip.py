#zip

#it zip the two or more  list and return tuple
user=["user1","user2","user3","user4"]
name={"parul","simran","sakshi"}
last_name=("sajwan","sajwan","negi")
 # print(dict(zip(user,name,last_name))) ''' it cannt be  convert into dict because it have 3 list  we neend only tow '''
print(list((zip(user,name,last_name))))