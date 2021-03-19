""" this is card game  to find the greater card """
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
# ankitksr: Correct the spacing here as per PEP guidelines.
digits=[]
suits=["D","S","H","C"]
cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# ankitksr: all variable names in python should be in snake_case
NumberOfPlayers=int(input("Enter Number of Player"))
for i in range(NumberOfPlayers):
    val=input().upper()
    if("".join(re.split("[^0-9]*",val)) in cards)or("".join(re.split("[^a-zA-z]*",val)) in suits):
        VALUE=int("".join(re.split("[^0-9]*",val)))
        digits.append(VALUE)
maximumval=max(digits)
<<<<<<< HEAD
=======
# print(digits)
# print(maximumval)

>>>>>>> 7d1420ecb65c5d9f8f6e03fc50cf2052b0548684
for i in digits:
    if maximumval==i:
        playerNo=digits.index(i)
        print(f"Winner of this game is player{playerNo+1}")
        