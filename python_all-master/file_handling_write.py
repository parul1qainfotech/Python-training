# f=open("parul.txt","w+")
# a=f.write("hello parul this is new text written by me thankyou")

#read and write mode both
f=open("parul.txt","r+")
f.write("\nthis is append mode")
print(f.read())
f.close()