# File Handling

import os

# getcwd()

# print(os.getcwd())

# chdir()

# os.chdir(r"C:\Users\ASUS\OneDrive\Documents\Desktop\Python")
#
# print(os.getcwd())

#mkdir()

# os.mkdir("SQL")

# os.mkdir("java")

# os.mkdir("React")

# rmdir()

# os.rmdir("React")

# popen()

os.popen("python.txt")

# rename()

# os.rename("SQL","SQlCode")

# remove()

# os.remove("python.txt")

# print(os.listdir())

# os.chdir(r"C:\Users\ASUS\OneDrive\Documents\Desktop\Python")
#
# print(os.path.getsize("java"))


# File Operations

# 1. r
# 2. w
# 3. a
# 4. x

# 1. without context manager

# var_name = open('fine_name','mode')

# x = open('RE.py','r')
#
# print(x.name)           #RE.py
# print(x.mode)           #r
# print(x.closed)           #False
# print(x.readable())          #True
# print(x.writable())         #False
# x.close()
# print(x.closed)         #True


# x = open("sample.txt",'w')
# print(x.write("Good morning"))           #12

# x = open("sample.txt",'r')
# print(x.read())       #Good morning
# os.popen("sample.txt")

# x = open("sample.txt",'w')
# print(x.writelines(["Hi, My name is Dhanshri.\nI am from Kolhapur.\nI have completed my B.Tech (Computer science) with 8.5 CGPA"]))
#
# os.popen("sample.txt")

# x = open("sample.txt",'r')
# print(x.readline())
# print(x.readlines())

# x = open("sample.txt",'a')
# print(x.write("My skills are Python, java,sql"))
# os.popen("sample.txt")