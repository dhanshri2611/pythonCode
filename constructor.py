# Constructor

# It is a special member of the class
# __init__()

# Types :
# 1. Default Constructor/ Predefined Constructor
# 2. User defined Constructor

# 1. Default Constructor/ Predefined Constructor
# class Bank:
#     def __init__(self):
#         name = "SBI"
#         ifsc = "SBI123"
#         area = "Pune"
#         print(f"My bank name is {name} and bank ifsc code is {ifsc} and location is {area}")
#
# b = Bank()
# b1  = Bank()
#
# Bank.__init__(b)

# 2. User defined Constructor

# class Bank:
#     def __init__(self,name,ifsc):
#         print(f"My bank name is {name} and bank ifsc code is {ifsc}")
#
# b = Bank("SBI","SBI678")


# instance variable
# Syntax
#     self.var_name = value

# When we use local var of init we use instance var

# class Exam:
#     def  __init__(self):
#         self.name = "Dhana"
#         self.roll_no = "12"
#         self.loc = "pune"
#         self.quali = "BE"
#
#     def student_details(self):
#         print(f"Student name is {self.name}. Roll no. is {self.roll_no}. Location is {self.loc} and qualification is {self.quali}")
#
#
# e = Exam()
# e.student_details()
# e.name= "Gk"
# e.student_details()
#
# Exam.name = "Rk"     #we can not update instnace varible using class name only update using object
# e.student_details()

# class Exam:
#     def  __init__(self,name,roll,loc,edu):
#         self.name = name
#         self.roll_no = roll
#         self.loc = loc
#         self.quali = edu
#
#     def student_details(self):
#         print(f"Student name is {self.name}. Roll no. is {self.roll_no}. Location is {self.loc} and qualification is {self.quali}")
#
#
# e = Exam("dhanu",12,"pune","BE")
# # e.student_details()
#
# # Exam.student_details(e)
#
# Exam.__init__(e,"gk",9,"kolhapur", "BE")
# Exam.student_details(e)


# Method overloading

# We cannot achieve method overloading in python we can achieve but partially using defaults

# class Details :
#     def add(self):
#         print("add1")
#
#     def add(self):
#         print("add2")
#
#     def add(self):
#         print("add3")
#
# d = Details()
# d.add()

# class Details:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(self.a+self.b)
#
#     def add(self):
#         print(self.a-self.b)
#
#     def add(self):
#         print(self.a*self.b)
#
# d = Details(1,2)
# d.add()

# class Details:
#     def __init__(self,a,b):
#         print(a+b)
#
#     def __init__(self, a, b):
#         print(a-b)
#
#     def __init__(self, a, b):
#         print(a*b)
#
# d = Details(1,2)

# class Details:
#     def __init__(self, a=0, b=0):
#         print(a + b)
#
#     def __init__(self, a=0, b=0):
#         print(a - b)
#
#     def __init__(self, a=0, b=0):
#         print(a * b)
#
#
# d = Details(1, 2)


# class Car:
#     def __init__(self,color,price,*args):
#         print(f"My color is {color} and price is {price} . My car name is {args}")
#
# s = Car("black",123123,"BMW")

class Student:
    def __init__(self,name,rollNo,*args):
        print(f"name= {name} rollNo = {rollNo} college = {args}")

s = Student("Dhanu",12,"SGMCOE","BE")