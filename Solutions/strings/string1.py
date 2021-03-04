# Count all lower case, upper case, digits, and special symbols from a given string
Chars=0
Digits=0
Symbol=0
str1 = "P@#yn26at^&i5ve"
for i in str1:
    if(i.isalpha()):
        Chars=Chars+1
    elif(i.isdigit()):
        Digits=Digits+1
    else:
        Symbol=Symbol+1
        
print("Chars:",Chars)
print("Digits:",Digits)
print("Symbol",Symbol)
    