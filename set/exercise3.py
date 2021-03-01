#Return a set of all elements in either A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))

#2nd way
# a=set1.difference(set2)
# b=set2.difference(set1)
# print(a.union(b))

#3rd way
# a=set1.intersection(set2)
# b=set1.union(set2)
# print(b-a)