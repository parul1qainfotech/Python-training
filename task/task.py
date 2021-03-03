import re
print('''
    For cards:   
      1.Diamond-D,d  2.Spade-S,s  3.Heart-H,h  4.Club-C,c 
      
    For cards number:
          Ace-1
          2
          3
          4
          5
          6
          7
          8
          9
          10
          Jack-11
          Queen-12
          King-13 ''')
digits=[]
suits=["D","S","H","C"]
cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
NumberOfPlayers=int(input("Enter Number of Player"))
for i in range(NumberOfPlayers):
    val=input().upper()
    if("".join(re.split("[^0-9]*",val))  in cards)or("".join(re.split("[^a-zA-z]*",val))  in suits):
        val2=int("".join(re.split("[^0-9]*",val)))
        digits.append(val2)
        
maximumval=max(digits)
# print(digits)
# print(maximumval)
for i in digits:
    if(maximumval==i):
        playerNo=digits.index(i)
        print(f"Winner of this game is player{playerNo+1}")
   
        
        

