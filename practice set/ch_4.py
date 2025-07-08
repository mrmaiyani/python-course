#1.wap to store seven fruits in a list entered by the user.
'''
Fruits = []

Fruits1 = input("Enter Fruit Name:")
Fruits.append(Fruits1)
Fruits2 = input("Enter Fruit Name:")
Fruits.append(Fruits2)
Fruits3 = input("Enter Fruit Name:")
Fruits.append(Fruits3)
Fruits4 = input("Enter Fruit Name:")
Fruits.append(Fruits4)
Fruits5 = input("Enter Fruit Name:")
Fruits.append(Fruits5)
Fruits6 = input("Enter Fruit Name:")
Fruits.append(Fruits6)
Fruits7 = input("Enter Fruit Name:")
Fruits.append(Fruits7)

print(Fruits)
'''

#2.wap to accept marks of 6 students and display then in sorted manner.
'''
marks = []

m1 = int(input("Enter 1st student marks:"))
marks.append(m1)
m2 = int(input("Enter 2nd student marks:"))
marks.append(m2)
m3 = int(input("Enter 3rd student marks:"))
marks.append(m3)
m4 = int(input("Enter 4th student marks:"))
marks.append(m4)
m5 = int(input("Enter 5th student marks:"))
marks.append(m5)
m6 = int(input("Enter 6th student marks:"))
marks.append(m6)

marks.sort()
print(marks)
'''

#3.check that tuple cannot change in python.
'''
a = (49,87.45,"radhe")

a[2] = "krishn"
'''

#4.wap to sum a list with 4 numbers.
'''
s = []

s1 = int(input("Enter 1st number:"))
s.append(s1)
s2 = int(input("Enter 2nd number:"))
s.append(s2)
s3 = int(input("Enter 3rd number:"))
s.append(s3)
s4 = int(input("Enter 4th number:"))
s.append(s4)

print(sum(s))
'''

#5.wap to count the number of zeros on the following tuple: a = (7,0,8,0,0,9)
a = (7,0,8,0,0,9)
print(a.count(0))