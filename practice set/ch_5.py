# 1. wap to create a dictionary of hindi words with values as their
#  english transaction.provide user with an option to look it up!
'''
words = {
    "Bahadur":"Brave",
    "Dayalu":"Kind",
    "Khush":"Happy"
}

word = input("Enter the word which meaning you want to know:")
print(words[word])
'''

#2. wap to input eight numbers from the user and display all the unique numbers(once).
'''
n = set()

n1 = int(input("Enter your number:"))
n.add(n1)
n2 = int(input("Enter your number:"))
n.add(n2)
n3 = int(input("Enter your number:"))
n.add(n3)
n4 = int(input("Enter your number:"))
n.add(n4)
n5 = int(input("Enter your number:"))
n.add(n5)
n6 = int(input("Enter your number:"))
n.add(n6)
n7 = int(input("Enter your number:"))
n.add(n7)
n8 = int(input("Enter your number:"))
n.add(n8)

print(n)
'''

#3.can we have a set with 18(int) and "18"(str) as a value in it?
'''
s = set()
s.add(18)
s.add("18")
print(s)
'''

#4.what will be the length of following set s:
'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
'''

#5.s = {} what is the type of s?
'''
s = {}
print(type(s))
'''

#6.create an empty dictionary.allow 4 friends to enter their fav. language
#  as values and use keys as their names. assume that the names are unique.
'''
friends = {}

name = input("Enter friend name: ")
language = input("Enter language name: ")
friends.update({name : language})

name = input("Enter friend name: ")
language = input("Enter language name: ")
friends.update({name : language})

name = input("Enter friend name: ")
language = input("Enter language name: ")
friends.update({name : language})

name = input("Enter friend name: ")
language = input("Enter language name: ")
friends.update({name : language})

print(friends)
'''

#7. if name of two friends are same;what will happen to the program in que.6?
'''
print("the value give later will be updated")
'''

#8. if language of two friends are same;what will happen to the prog. in que.6?
'''
print("nothing will be happen,the value can be same")
'''

#9.can you change the value inside a list which is contained in set s.
#  s = {8,7,12,"radhe",[1,2]}

print("this is invalid")
