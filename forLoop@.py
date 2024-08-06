# 1.wap to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"
# d = {}
# l = s.split()
# for i in l:
#     d[l.index(i)]= i
# print(d)

# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

# 2.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"
# l = s.split()
# d = {}
# for i in l :
#     d[i] = len(i)
# print(d)

# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}

# # 3.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"
# d = {}
# for i in s:
#     d[i] = i.upper()
# print(d)

# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

# 4.wap to create a dictionary Ascii and character pair
# l = [89,51,111,77,108,120]
# d = {}
# for i in l:
#     d[i]= chr(i)
# print(d)

# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}

# 5.wap to  create a list of characters and its Ascii value pair
# s="sunday"
# l = []
# j = ()
# for i in s:
#     j = (i,ord(i)])
#     l.append(j)
# print(l)

# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]

# 6.WAp to perform clear() in list without using inbuilt method
# lst= ['hai', 'hello', 'python', 'world', 'jingalala']
# for i in range(len(lst)):
#     lst.pop()
# print(lst)

# 7.wap to create a dictionary with words and its length pair and ends with vowel
# s="Today is Tuesday and attending python session"
# d = {}
# for i in s.split():
#     if i[-1] in("a","e","i","o","u"):
#         d[i]=len(i)
# print(d)

# 8.wap to create a dictionary with letter and its words starting with that letter pair
# s="hi hello good morning welcome to python session"
# d = {}
# for i in s.split():
#     l = []
#     for j in s.split():
#         if j[0]==i[0]:
#             l.append(j)
#     d[i[0]] = l
# print(d)

# for i in s.split():
#     if i[0] in d:
#         d[i[0]] += [i]
#     else:
#         d[i[0]] = [i]
# print(d)

# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

# 9.wap to create a dictionary of characters and its indices pair

# s="hello python"
# d = {}
# for i in range(len(s)):
#     if s[i] not in d:
#         d[s[i]] = [i]
#     else:
#         d[s[i]] += [i]
# print(d)

# o/p:-->{"h":[0,9],"e":1..........}

# 10.wap to using this list get the below output
# l = ['sun flower', 'lily flower', 'Marigold flower', 'lion animal','tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# d = {}
# for i in l:
#     s = i.split()
#     if s[1] in d :
#         d[s[1]] += [s[0]]
#     else:
#         d[s[1]] = [s[0]]
# print(d)

# o/p:-->{'flower': ['sun', 'lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}

# 11.wap to sum of same index element from
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=[11,12,13,14,15]
# l = []
# for i in zip(l1,l2,l3):
#     sum = 0
#     for j in i:
#         sum += j
#     l.append(sum)
# print(l)

# 12.wap to pair values of both dictionary

# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
# l = []
# for i in zip(d.values(),p.values()):
#     l +=[i]
# print(l)

# 13.wap to group fruit name and country pair only if a fruit is even length

# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
# l = []
# for i in zip(d.keys(),p.keys()):
#     if len(i[0])%2==0:
#         l +=[i]
# print(l)

# 14.WAP to check whether string is ANAGRAM or not (anagrams : characters should be same it can different meaning)
# take user input
# s = str(input("Enter the String : "))
# s1 = str(input("Enter the String : "))
# ct = 0
# if len(s) == len(s1):
#     sct = {}
#     s1ct = {}
#     for i in s.lower():
#         if i in sct:
#             sct[i] +=1
#         else:
#             sct[i] =1
#
#     for i in s1.lower():
#         if i in s1ct:
#             s1ct[i] += 1
#         else:
#             s1ct[i] = 1

#     if sct == s1ct:
#         print("It is anagram")
#     else:
#         print("it is not ana anagram")
# else :
#     print("Not anagram")

# a = "abc"
# b = "ba"
# a = sorted(a.lower())
# b = sorted(b.lower())
# if a==b:
#     print("Its anagram")
# else:
#     print("Not anagram")

# 15.WAp to print longest word in a sentence

# s = 'life is full of surprises and miracles'
# long = ""
# for i in s.split():
#     if len(long)<len(i):
#         long = i
# print(long)

# #exp o/p : surprises

# 16.Replaces whitespaces with new line char in the below string
# s = 'hello world welcome to python'
# for i in s:
#     if i.isspace():
#         s = s.replace(i,"\n")
# print(s)

# 17.wap to check  whether the elements inside the list is even or odd and i want the dictionary pair

# l=["apple","samsung","oracle","flipkart","facebook","instagram","amazon","ebay"]
# d = {}
# for i in l:
#     if len(i)%2==0:
#        if "even" not in d:
#            d["even"] = [i]
#        else:
#            d["even"] += [i]
#     else:
#         if "odd" not in d:
#             d["odd"] = [i]
#         else:
#             d["odd"] += [i]
# print(d)

# o/p:-->{'odd': ['apple', 'samsung', 'instagram'], 'even': ['oracle', 'flipkart', 'facebook', 'amazon', 'ebay']}

# 18.wap to traverse through a string and stop the execution at specific characters by using break keyword

# s="hello guys tomorrow holiday"
# specified_char="d"
# for i in s:
#     if i == specified_char:
#         break
#     print(i,end="")

# 19.wap to print double digit numbers present in list by using continue keyword
# l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]
# for i in l :
#     if i<9:
#         continue
#     print(i,end=" ")

# 20.wap to print only positive numbers by using continue keyword

# l=[1,5,-2,-45,55,88,-100,-63]
# for i in l:
#     if i<0:
#         continue
#     print(i)

# 21.wap to skip all the vowels in the given string

# s="good morning guys welcome to python session"
# for i in s:
#     if i in ("a","e","i","o","u"):
#         continue
#     print(i,end= " ")
