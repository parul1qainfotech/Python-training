#Print the following pattern:
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

number=int(input("enter the number"))
for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")