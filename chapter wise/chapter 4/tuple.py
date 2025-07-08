a = (1,342,45,342,1234,False,342,"Utsav","Yug")
b = (2,5,44,36)
print(a)
# imp note : tuple can not change value on tuple 
print(type(a))
b = (1) #this is integer
c = (1,) #this is tuple
print(type(b))
print(type(c))

count = a.count(342)
print(count)
index = a.index(342)
print(index)

print(len(a))
print(max(b))