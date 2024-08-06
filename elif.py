#1. check given number is -ve/+ve/neutral

# num = int(input("Enter the number : "))
# if num>0 :
#     print("+ve")
# elif num==0 :
#     print("neutral")
# else :
#     print("-ve")

# 2.check the given character is upper/lower/digit/special

# ch = eval(input("Enter the character : "))
# if ch.isupper():
#     print("is upper")
# elif ch.islower():
#     print("is lower")
# elif ch.isdigit():
#     print("is digit")
# else:
#     print("is special")

# ch = eval(input("Enter the character : "))
# if "A"<=ch<="Z":
#     print("is upper")
# elif "a"<=ch<="z":
#     print("is lower")
# elif "0"<=ch<="9":
#     print("is digit")
# else:
#     print("is special")

#3.wap to check a data is a sequence/iterable/individual data type

# data = eval(input("Enter the data : "))
# if isinstance(data,(bool,int,float,complex)):
#     print("It is a individual data type")
# elif isinstance(data,(str,list,tuple)):
#     print("It is a sequence data type")
# else:
#     print("it is a iterable")

# 3.wap if input is string return its length,else if input is list pop element,else
#  if input is tuple reverse else invalid input

# s = eval(input("Enter the input : "))
# if isinstance(s,str):
#     print(len(s))
# elif isinstance(s,list):
#     print(s.pop())
# elif isinstance(s,tuple):
#     print(s[::-1])
# else:
#     print("invalid")

# 4.wap to check a age belongs to category 0 to 17 child and 18 to 30 ur adult,31 to 60 ur men,61 to 100 senior citizen,else
#  invalid
# age = int(input("Enter the age : "))
# if age>=0 and age<=17:
#     print("ur child")
# elif age>=18 and age<=30 :
#     print("ur adult")
# elif age>=31 and age<=60 :
#     print("ur men")
# elif age>=61 and age<=100:
#     print("ur citizen")
# else:
#     print("invalid")
#

# 5.wap to give hike to an employee based on his experience,u should ask employee date of joining
#  exp 0 to 2 years no hike and 3 to 5 years 5000rs hike,and 6 to 8 years 7000 rs and 9 to n years 10000 rs
# joining =eval(input("Enter joining date : "))
# year = eval(input("Enter year : "))
# ex=(year-joining)
# if ex<=2 and ex>=0 :
#     print("no hike")
# elif ex>=3 and ex<=5:
#     print("salary hike 5000")
# elif ex>=6 and ex<=8:
#     print("salary hike 7000")
# else :
#     print("salary hike 10000")

# 6.wap to check which is smallest value among 3 numbers
# a=65  b=34  c=76

# a,b,c=61,34,76
# if a<b and a<c:
#     print(f"{a} is smallest")
# elif b<a and b<c :
#     print(f"{b} is smallest")
# else :
#     print(f"{c} is smallest")


# 7.wap to take marks of 5 sub,calculate the average if the average is b/w 90-100 print Distinction
# if 75-89 print first class and if it's 60-74 print second class, if 50-59 print Third class,below 50 is fail
# note:-->max marks is 100

# s1,s2,s3,s4,s5 = 1,1,1,1,1
# avg = ((s1+s2+s3+s4+s5)*100)/500
# if 90<=avg<=100:
#     print("Distinction")
# elif 75<=avg<=89:
#     print("First class")
# elif 60<=avg<=74:
#     print("second class")
# elif 50<=avg<=59 :
#     print("third class")
# else :
#     print("fail")

# 8.wap to check the char is uppercase or lowercase or digit or special character (using inbuilt function)


