#set & method
'''
empty_set = set() # not use {} bcz this is use to empty dict.
set = {1,45,67,5,5,46,5,'radhe'}

print(set,type(set))
set.add(402)
print(set,type(set))
set.remove(402)
print(set,type(set))
'''

# union & inter section
s1 = {1,3,5,7,2}
s2 = {2,3,6,8,9,11}

print(s1.union(s2))
print(s1.intersection(s2))