import re

# 1. match()
# Syntax -->
# var_name=re.match(pattern,source_string)

# s = "Dhanshri Vilas Kasalkar"
# x = re.match("Dhanshri",s)
# print(x)              #<re.Match object; span=(0, 8), match='Dhanshri'>
#
# x1 = re.match("Vilas",s)
# print(x1)  #None

# 2. fullmatch()
# Syntax
# var_name= re.fullmatch(pattern,source_String)

# s = "Python is a high level programming language"
# x = re.fullmatch("Python",s)
# print(x)    #None
#
# x1 = re.fullmatch("Python is a high level programming language",s)
# print(x1)      #<re.Match object; span=(0, 43), match='Python is a high level programming language'>

# 3. search()
# Syntax -->
# var_name=re.search(pattern,source_string)

# s = "Python is a high level programming language"
# x = re.search("t",s)
# print(x)     #<re.Match object; span=(2, 3), match='t'>

# 4. sub()
# Syntax -->
# var_name=re.sub(pattern,source_string)

# s = "Python is a high level programming language"
# x = re.sub(" ","_",s )
# print(x)   #Python_is_a_high_level_programming_language

# x1 = re.sub("p","P",s,100)
# print(x1)     #('Python is a high level Programming language', 1)

# 5. subn()
# Syntax -->
# var_name=re.subn(pattern,source_string)

# s = "Python is a high level programming language"
# x = re.subn("l","L",s)
# print(x)              #('Python is a high LeveL programming Language', 3)
#
# x1 = re.subn("p","P",s,100)
# print(x1)     #('Python is a high level Programming language', 1)


# 6. split()
# Syntax -->
# var_name=re.split(pattern,source_string)

# s = "Python is a programming language"
# x = re.split(" ",s)
# print(x)            #['Python', 'is', 'a', 'programming', 'language']

# x1 = re.split("i",s,maxsplit=1)
# print(x1)

# 7.findall()
# Syntax -->
# var_name=re.findall(pattern,source_string)

# s = "Python is a High Level Programing language 123"
# x = re.findall("[a-z]", s)
# print(x)
#
# x1 = re.findall("[A-Z]", s)
# print(x1)
#
# x2 = re.findall("[0-9]", s)
# print(x2)
#
# x3 = re.findall("\w", s)
# print(x3)
#
# x4 = re.findall("\W", s)
# print(x4)
#
# print(re.findall("\d", s))
#
# print(re.findall("\D", s))
#
# print(re.findall("\.", s))
#
# print(re.findall("\s", s))
#
# print(re.findall("\S", s))
#
# print(re.findall("^",s))



# # 1. matches any number between 0-9
# a = "The cost of the book is Rs.100"
# print(re.findall("\d",a))

# 2. matches only lower case letter and upper case letter

# b = "hello HOW ARE YOU"
# print(re.findall("[a-zA-Z]",b))

# 3. Wap to count the number of white space in a given string

# c = "HELLO world welcome to python Hi how are you. Hi how are you"
# print(len(re.findall(" ",c)))

# 4. Sum all the numbers in the below string

# word = "PYTHON12nREG567exp2"
# x = re.findall("\d",word)
# print(x)
# sum = 0
# for i in x:
#     sum +=int(i)
# print(sum)

# 5. matches everything apart from between 0-9

# a = "The cost of the book is Rs.100"
# print(re.findall("\D",a))

# 6. matches everything apart from "a","b","c","d"

# b = "abcdefghijklmnop"
# print(re.findall("[^abcd]",b))

# 7.matches only those charactyers accepts digit

# word = "@hello2world34welcome!123"
# print(re.findall("\D",word))

#8.extracting file with extension

# s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
#
# print(re.findall("[A-Za-z]+\.[A-Za-z]+",s))


#9.wap to extract only pincode

# s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# print(re.findall(r'\b[0-9]{6}+\b',s))


# 10.wap to print the AADHAR CARD numbers

# s="my Aadhar number is 1234-4567-8910"
# print(re.findall(r'[0-9]{4}+-+[0-9]{4}+-+[0-9]{4}',s))

# 11.wap to print the pan card number

# a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
# print(re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a))

# 12.How to fetch the protocols

# a="https://www.google.com"
# print(re.findall(r'[a-z]+',a))
# print((a))

# o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
# o/p--->['https://www.google.com']        (second output)
#
#
#
# 13.creating acronyms of the file format
#
# file_format=["Graphic Interchange Format",
#               "Advanced Audio Coding",
#             "HyperText Markup Language",
#              "Content Management System",
#             "Windows Media,Audio",
#             "Comma Separated values"]
# for i in file_format:
#     match = re.findall("[A-Z]",i)
#     print(''.join(match))



# o/p-->GIF,AAC,HTML,CMS,WMA,CSV


# 14.wap to match email ids

# emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]
# for i in emails:
#     if (re.match(r'[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]',i)):
#         print(i)



# 15.matching phone numbers

# phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]
# for i in phonenumbers :
#     if(re.match('[0-9]{3}-[0-9]{3}-[0-9]{4}',i)):
#         print(i)

# 16.replace whitespace with newline characters

# s="helloworld welcome to python"
# print(re.sub(' ','\n',s))


# 17.replace all digits with **

# s="hello 123 mic testing 123 123"
# print(re.sub('[0-9]','**',s))


s = "dfghj"
s= 'ghjkl'
print(s)
s.replace('h','g',1)
print(s)