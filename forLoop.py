#For Loop
# for ref_var in collection/iterable :
#   statement

# Using range()
#
# for in range(si,ei+1,sv):
#     statement

#enumrate()

# Syntax : enumerate(iterable)

#reversed()

# Syntax : reversed(iterable)

#zip()

# Syntax : zip(iterable)

#zip_longest()

# Syntax :

    # from itertools import zip_longest

    # zip_longest(iterable)


#List

# a = [1,2,3,4]
# for i in a:
#     print(i,end=" ")

#String
# s = "Good Morning"
# for i in s:
#     print(i,end=" ")

#tuple

# t = (1,2,3,4,5)
# for i in t:
#     print(i,end=" ")

#set

# s = {1,2,3,4,67}
# for i in s:
#     print(i,end=" ")

#dictionary

# d = {1:"a",2:"b",3:"c"}
# for i in d:
#     print(i,end=" ")

# for i in d.values():
#     print(i,end=" ")

# for i in d.items():
#     print(i,end=" ")

#enumrate

# e = [1,2,3,4,5,6]

# it gives the object address
# print(enumerate(e))
# print(list(enumerate(e)))

# for i in enumerate(e):
#     print(i,end=" ")

# for i,j in enumerate(e):
#     print(i,end=" ")

# for i, j in enumerate(e):
#     print(i,j,end=" ")

#reversed

# r = "Good morning"
r = ['sdf','sdv']
print(reversed(r))
print(list(reversed(r)))

for i in reversed(r):
    print(i,end="")

# r[::-1]
# print(r)

#zip

# z = [1,2,3,4,5]
# a = ["a","b","c","d","e"]
# print(zip(z,a))
# print(list(zip(z,a)))

# for i in zip(z,a):
#     print(i)

# z = [1,2,3,4,5]
# a = ["a","b","c"]

# for i in zip(z,a):
#     print(i, end="")

#zip_longest

# from itertools import  zip_longest

# for i in zip_longest(a,z):
#     print(i,end="")

# from itertools import  zip_longest
# for i in zip_longest(z,a, fillvalue="Hi"):
#     print(i,end="")

# print the number upto 20

# for i in range(21):
#     print(i)

# for i in range(0,21,1):
#     print(i, end=" ")

# a = ["a","b","c","d","e"]
# for i in range(len(a)):
#     print(i)

# s = "Dhanshri"
# for i in range(len(s)):
#     print(s[i],i, end=" ")

# ***************************************************************

# 1.wap to print the number form 1 -20 segregate even and odd number into list

# odd=[]
# even=[]
# for i in range(1,21,1):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# 2.wap to extract vowels and digits in a string

# s="hello123"
# for i in s:
#     if i in ("a","e","i","o","u") or i.isdigit():
#         print(i,end=" ")

# 3.wap to capitalize only the first letter of every word in the given list

# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l :
#     print(i.capitalize(),end=" ")

# 4.wap to extract only individual data types form the list

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if type(i) in (int,bool,complex,float):
#         print(i,end=" ")

# 5.wap to extract only individual data types from the list and sum all the individual data types

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum = 0
# for i in l:
#     if type(i) in (int,float,bool,complex):
#        sum+=i
# print(sum)

# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"
# alph = 0
# num = 0
# space = 0
# for i in s:
#     if i.isdigit():
#         num+=1
#     elif i.isalpha():
#         alph+=1
#     elif i.isspace():
#         space+=1
# print(f"Alphabets : {alph} Numbers : {num}, Spaces : {space}")


# 7.wap to check how many words are present in the given sentence

# s="hello world sentence"
# word = 0
# s=s.split()
# print(s)
# for i in range(len(s)):
#     word+=1
# print(word)

# 8.wap to create a dictionary and print the characters and its Ascii value pair

# s="hello world"
# d = {}
# for i in s:
#     d[i]=ord(i)
# print(d)
# output:--> {"h":ascii value,"e":ascii value........}


# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it

# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d = {}
# for i in names:
#     if len(i)%2==0:
#         d[i]=len(i)
#     else:
#         d[i]=i[::-1]
# print(d)

# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

# 10.wap to print series of factorial(take user input)

# num = int(input("Enter the number : "))
# fact = 1
# for i in range(fact,num+1):
#     fact*=i
# print(fact)

# 11.wap to create a dictionary with element and its count pair

# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# d = {}
# for i in l:
#     d[i]=l.count(i)
# print(d)

# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

# 12.wap to find the length of the string without using inbuilt function

# s="Never Give Up"
# length=0
# for i in s:
#     length+=1
# print(length)

# 13.wap to reverse a string without using inbuilt function

# x="you did it guys"
# rev = ""
# for i in x:
#     rev = i+rev
# print(rev)

# 14.wap to print alternative character from a given string

# s="hello python"
# for i in range(0,len(s),2):
#     print(s[i],end="")

# 15.wap to replace all the character with "-" if the characters occurs more than once in a string

# s="hellohai"
# for i in s:
#     if s.count(i)>1:
#        s = s.replace(i,"-")
# print(s)

# o/p---->-e--o-ai

# 16.wap to get  output:--->1234 in below question

# t=("1","2","3","4")
# op = ""
# for i in t:
#     op+=i
# print(op)

# 17.wap to Sum of numbers

# s = 'Sony12India567pvt21ltd'
# sum = 0
# for i in s:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# 18.WAP to print sum of internal and external list

# l = [[1,2,3], [4,5,6], [7,8,9]]
# a = []
# external = 0
# for i in l:
#     internal = 0
#     for j in i:
#         internal+=j
#     a.append(internal)
#     external+=internal
# print(f"Internal = {a}")
# print(f"External = {external}")

# output:-->
#    #internal = 6, 15, 24
#    #external --> 45
#
# 19. WAP to remove duplicates from the list without using inbuilt function

# d=[1,2,3,4,5,6,7,1,2,3,4]
# duplicate = []
# non_duplicate = []
# for i in d :
#     if i not in duplicate:
#         duplicate.append(i)
#     else :
#         non_duplicate.append(i)
# print(non_duplicate)
# print(duplicate)

# 20.Print all the missing numbers from 1-10 in the below list

# l = [1, 2, 3, 4, 6, 7, 10]
# a = []
# for i in range(1,11,1):
#     if i not in l:
#         a.append(i)
#     else:
#         a.append(i)
# print(a)

# for i in range(1,11):
#     if i not in l:
#         a.append(i)
# print(a)


# 21.Reverse a list without using any built-in functions and slicing.

# l = [1, 2, 3, 4]
# rev = []
# for i in range(len(l)-1,-1,-1):
#     rev +=[l[i]]
# print(rev)

# for i in l:
#     rev = [i]+rev
# print(rev)


# 22.wap to get below out put

# s="Hi How are you"
# op = ""
# for i in s:
#     op = i + op
# print(op)

# o/p-->"uoy era woH iH'

# 23.wap to print repeated char and count the same

# s="helloword"
# d={}
# for i in s:
#     if s.count(i)>1:
#         d[i]=s.count(i)
# print(d)

# o/p{'l': 2, 'o': 2}

# 24.wap to filter out even and odd numbers in the given string

# s="hello 123 world 456 welcome to python1234567"
# even = " "
# odd = " "
# for i in s:
#     if i.isdigit():
#         if int(i)%2==0:
#             even+=i
#         else:
#             odd+=i
# print(f"Even : {even} Odd : {odd}")

# 25.,wap to create a dictionary word and reverse word pair

# s="tomorrow is weekend and non-veg special"
# d = {}
# for i in s.split():
#     d[i] = i[::-1]
# print(d)

# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}
