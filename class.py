# Syntax:
# class Class_name:
#
#     variable/class_variable
#     class_method
#     constructor


# variable:
# 1. Local variable
# 2. Global variable
# 3. Instance variable

# Method
# 1. Instance Method
# 2. Class method
# 3.Static method

# 1.Instance method : instance = object
#         Any method it will accept object address as an arg is called instance method

# class Class_name:
#     def fun_name(self):   #self is a special parameter
#         stmt
#
# variable =  Class_name()      # here varible is a object address which is pointing to the self

# class Sample:
#     def demo(self):
#         print("Good morning")
#
# s = Sample()
# s.demo()                #By calling object
#
# Sample.demo(s)      # by calling class name


# Without Argument

# class Employee:
#     def details(self):
#         sal = 10000           #Local variable
#         print(f"My salary is {sal}")
#         print(self)       #<__main__.Employee object at 0x0000023259DF7B00>
#
# e = Employee()
# # e.details()
#
# Employee.details(e)
# print(e)         #<__main__.Employee object at 0x0000023259DF7B00>


# With argument
# class Employee:
#     def details(self,name,sal):
#         print(f"My name is {name} and my salary is {sal}")
#
# e = Employee()
# e.details("dhana",100000)
#
#
# Employee.details(e,"Dhanu",12345)


# class Flipkart:
#     product ='watch'
#     price=2333
#     loc = 'pune'
#
#     def order(self):
#         print(f"my product name is {self.product} and price is {self.price}")
#
#     def delivery(self):
#         print(f"my location is {self.loc}")
#
# f = Flipkart()
#
# f.order()
# f.delivery()

# class Amazon:
#
#     product = "watch"
#     def order(self,name,loc):
#         print(f"my name is {name} and price is {loc} and product is {self.product}")
#
# a = Amazon()
# a.order("Dhana","pune")

# class PYSPIDER:
#     subject = "Python"
#     toatal_student=22
#     c_duration= "2 month"
#     loc = "Deccan"
#
#     def

# wap to accept list from the user when method is call , 1st index ele in list if it is string then reverse the string
# then replace in same position and return else if it is a integer then ask for user to add a ele into a list and return
# the updates list else reverse the list and return


# class Check:
#     def s(self,l):
#         if isinstance(l[1], (str)):
#             l[1] = l[1][::-1]
#             return l
#         elif isinstance(l[1],int):
#             data = eval(input( ))
#             l.append(data)
#             return l
#         else:
#             return l[::-1]
#
# c = Check()
# print(c.s([1,"he",2,3,4]))

# 2. Class method
# Any method decorate with @classmethod is called as class method
# To creating alternative constructor of the class

# Syntax:
#      class Class_name:
#          @classmethod
#          def function_name(cls):
#              stmt
#
#      var = Class_name()

# Ex1.

# class Test:
#     @classmethod
#     def spam(cls):
#         print("Hello")
#
#         print(cls)           #<class '__main__.Test'>  cls pointing to the main class
#
#
# t = Test()
#
# t.spam()      #by calling object
#
# Test.spam()         #by calling class name
#
# print(t)               #<__main__.Test object at 0x0000024B55EE5B20>


# Ex2.
# class Student:
#     @classmethod
#     def details(cls,name,loc,phone):
#         print(f"My name is {name}. I am from {loc}. my contact number is {phone}")
#
#
# s = Student()
#
# s.details("Dhana", "Pune",7447899709)

# Ex3.

# class Election:
#     date = "26/05/2024"
#
#     @classmethod
#     def area1(cls):
#         print(f"my area election date is {cls.date} ")
#
#         # print(f"my area election date is {e.date} ")
#     @classmethod
#     def area2(cls):
#
#         x = cls()
#         x.date = "01/09/2024"
#         print(f"my area election date is {x.date} ")
#
#
# e = Election()
#
# # e.date = "01/01/2024"
# e.area1()
# e.area2()


# class VTO:
#
#     date = "01/02/2024"
#
#     @classmethod
#     def clg1(cls):
#         print(f"Exam date is {cls.date}")
#
#
#     @classmethod
#     def clg2(cls):
#         x= cls()
#         x.date = "02/02/2024"
#         print(f"Exam date is {x.date}")
#
#     @classmethod
#     def clg3(cls):
#         print(f"Exam date is {clg.date}")
#
#
#
#
# clg = VTO()
#
# clg.date = "05/01/2024"
# clg.clg1()
# clg.clg2()
# clg.clg3()

# 3. static method

# Ex1

# class Test:
#     @staticmethod
#     def demo():
#         print("Hello")
#
# t = Test()
#
# t.demo()

class Test1:
    start_date = "02/05/2024"

    @staticmethod
    def demo():
        print(f"The staring date of test is {Test1.start_date}")


t1 = Test1

t1.demo()

t1.start_date = "01/01/2025"

t1.demo()

# class GYM:
#     tread_mill = "25km"
#
#     @classmethod
#     def men_workout(cls):
#         print(f"men workout is {cls.tread_mill}")
#
#     @staticmethod
#     def women_workout():
#         print(f"Women workout is {GYM.tread_mill}")
#
# g = GYM()
#
# g.tread_mill = "100km"
# g.men_workout()
# # g.women_workout(g)
# g.women_workout()

# Create class as a bank and declare all the bank name, bank address, IFSC code, phone number as class
# variable and a create a class method and print all the bank general details for the all the customer


# Write a python program that define class called book the book class should have the following
# title, author and year . it should also have a class attribute books which is a list of all the book objects that have
# been created


# WAPP that defines a class called vehicle, the vehicle class should have the following attributes
# car name, model and year, and it should also have class attribute count, which keeps track of the number of vehicle
# objects that have been created


# Wp
