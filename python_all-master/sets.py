# unordered set of unique item

# in set we can store list tuple or dict
s={1,2,3,1,2,4,'parul'}
print(s)# printunique items

l=[1,2,3,4,2,2,2,6,7,1,1,4]
ll=list(set(l))
list(ll)
print(ll)

# add
s.add(6)
print(s)
#remove
s.remove(3)
# s.remove(5)     # it shows the error because not in the set
print(s.discard(5)) # doesnt give error give none


# clear method
s.clear()
print(s)

#copy of set

s2=s.copy()


'''my={[1,2]} # cant add list dict or tuple  
print(my)'''
