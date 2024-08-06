#wap to print 1 to 10 numbers

# i = 1
# while i<=10 :
#     print(i)
#     i+=1


#only print the list

# a= ["hello",[1,2,3],11,3+4j]
# i=0
# while i<len(a):
#     if isinstance(a[i],(list,str)) :
#         print(a[i])
#     i+=1


#table

# num = int(input("Enter the number : "))
# i=1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1

#Print character with its posituion

# a="Hello World!!"
# i = 0
# while i<len(a):
#     print(f"{a[i]}----{i}")
#     i+=1


# a="Hello World!!"
# i = 0
# while i<len(a):
#     print(a[i], i ,end=" ")
#     i+=1

# 10 to 1
# i = 10
# while i>=1 :
#     print(i)
#     i-=1

#wap to print characters and position

# a = "hello guys good morning"
# i = 0
# while i<len(a):
#     print(a[i],i, end=" ")
#     i+=1

# 1,wap to print series of 20 natural numbers

# n = 1
# while n<=20:
#     print(n)
#     n+=1

# 2.wap to print series of upper case characters
#output:--.A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# start = ord("A")
# end= ord("Z")
#
# while start<=end:
#     print(chr(start))
#     start+=1

# 3.wap to print series of lower case characters

#output:-->a b c d e f g h i j k l m n o p q r s t u v w x y z

# start = ord("a")
# end= ord("z")
#
# while start<=end:
#     print(chr(start))
#     start+=1


# 4.wap to print both upper and lower case characters

#output:-A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z

# start = ord("A")
# end = ord("z")
# while start<=end :
#     if 65<=start<=90 :
#         print(chr(start),end=" ")
#         start+=1
#     elif 97<=start<=122 :
#         print(chr(start), end= " ")
#         start+=1
#     else:
#         start+=1

# i = ord("A")
# j = ord("a")
# while i<=ord("Z"):
#     print(chr(i),chr(j), end=" ")
#     i+=1
#     j+=1


# 5.wap to print series of even numbers till 20 in reverse order

# output:->20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

# i=20
# while i>0:
#     if i%2==0:
#         print(i,end=" ")
#         i-=2

# 6.wap to count numbers of occurrence of specified elements in the collection
# s = 'Hello guys Good morning python is a programming language'

# i = 0
# a = eval(input("Enter the element : "))
# while i<len(s):
#     i+=1
# print(a, s.count(a), end=" ")

# i = 0
# a = eval(input("Enter the element : "))
# ct=0
# while i<len(s):
#     if s[i]==a:
#         ct+=1
#     i+=1
# print(a, ct, end=" ")

# 7.wap to print even positional characters in the given string

# output:-->h l o w r d
# s = "hello world"
# i = 0
# while i<len(s):
#     if i%2==0 :
#         print(s[i],end=" ")
#     i+=1

# 8.wap to display the position of the substring
# s= 'Hello guys Good morning python is a programming language'
#
# sub = input("Enter thr String : ")
# # i = 0
# # while i<len(s):
# #     if sub in s:
# #         pos=(s.index(sub))
# #     i+=1
# # print(pos)
#
# i = 0
# while i<len(s):
#     if s[i:i+len(sub)]==sub:
#         pos = i
#     i+=1
# print(pos)


#9.wap to print the number Table by using data given by user (take user input)
#expected output:-->2*1=2  2*2=4............2*10=20

# num = int(input("Enter the number : "))
# i=1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1

#10.wap to print the names only if the length of the names is even
# l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]

# i = 0
# while i<len(l):
#     if len(l[i])%2==0:
#         print(l[i])
#     i+=1

#11.wap to print the elements which in tuple, print only the if it is collection data types
# values=(10,2.5,[10,20],"hero", True,(3,4,5),{2,7},{90:"super"})
# i = 0
# while i<len(values):
#     if type(values[i]) in (list,str,set,dict,tuple):
#         print(values[i])
#     i+=1

#12.wap to print the name which is starting with vowel in the given list
# names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
# i = 0
# while i<len(names):
#     if names[i][0] not in ("a","e","i","o","u"):
#         print(names[i])
#     i+=1


#13.wap to print sum of numbers in the list
# l=[2,4,6,7,8,9]
# i = 0
# sum = 0
# while i<len(l):
#     sum+=l[i]
#     i+=1
# print(sum)

#14.wap to extract only vowels and digits from the given string
# s="hellopython123"
# i = 0
# while i<len(s):
#     if s[i] in ("a","e","i","o","u") or s[i].isdigit():
#         print(s[i])
#     i+=1

#15.wap to iterate inside the list check if it is having nested list if yes merge it

list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]

i = 0
while i<len(list1):
    if type(list1[i]) == list :
        li = list1.pop(i)
        list1 =list1+li
    i+=1
print(list1)

#excepted output:-->list1=["hello",10,20.55,True,False,"hai","bye",False,"goodnight","enjoy the holiday"]

#
# 16.wap if a names ends with vowels then reverse a names else print its length
# names=["Kumar","Lakita","Umesh a","Priyanka"]
# i = 0
# while i<len(names):
#     if names[i][-1] in ("a","e","i","o","u") :
#         print(names[i])
#     i+=1


# 17.wap to print all individual data type from list
# data=[34,"hai",3+4j,(1,2),{3,4},False,3.4]
# i = 0
# while i<len(data):
#     if type(data[i]) in (int,float,bool,complex):
#         print(data[i])
#     i+=1

# 18.wap to print each characters from a string

# s="python masters"
# i = 0
# while i<len(s):
#     print(s[i],end=" ")
#     i+=1

