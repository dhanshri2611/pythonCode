# Inheritance
# It is process of taking properties of one class to another class


# 1. Single Level Inheritance

# class Dad:
#     def vill(self):
#         print("Its Dad Villa")
#
# class Son(Dad):
#     def money(self):
#         print("Its party time")
#
# s = Son()
# s.vill()
# s.money()
# print(dir(Dad))
# print(dir(Son))

# 2. Multi Level Inheritance

# class Grandpa:
#     def vill(self):
#         print("Its grandpa villa")
#
# class Dad(Grandpa):
#     def car(self):
#         print("its Dad car")
#
# class Son(Dad):
#     def money(self):
#         print("Its party Time")
#
# s = Son()
# s.car()
# s.money()
# s.vill()
#
# print(dir(Son))
# print(dir(Dad))
# print(dir(Grandpa))

# 3. Multiple inheritance

# class Dad:
#     def money(self):
#         print("Its dad money")
#
# class Mom:
#     def cooking(self):
#         print("Good Cooking")
#
# class Son(Dad,Mom):
#     def bike(self):
#         print("Its son bike")
#
# s = Son()
# s.bike()
# s.cooking()
# s.money()
#
# print(dir(Son))
# print(dir(Dad))
# print(dir(Mom))

# 4. Hierarchical Inheritance

# class Dad:
#     def money(self):
#         print("Its dad money")
#
# class Son(Dad):
#     def bike(self):
#         print("Its Son Bike")
#
# class Daughter(Dad):
#     def education(self):
#         print("Education")
#
# s = Son()
# s.money()
# s.bike()
#
# print(dir(Son))
# print(dir(Dad))
#
# d = Daughter()
# d.education()
# d.money()
# print(dir(Daughter))


# super().method_name()

# it is used to avoid method override
# 
# class Sample:
#     def __init__(self):
#         print("Test Method")
# 
# class Demo(Sample):
#     def __init__(self):
#         print("Demo Method")
# 
# d = Demo()


# class Sample:
#     def __init__(self):
#         print("Test Method")
#
# class Demo(Sample):
#     def __init__(self):
#         super().__init__()
#         print("Demo Method")
#
# d = Demo()

# class Student:
#     def __init__(self,name,phone,loc):
#         print(f"My name is {name}. My contact Number is {phone}. My location is {loc}")
#
# class Stud(Student):
#     def __init__(self,name,phone,loc,sub,staff):
#         super().__init__(name,phone,loc)
#         print(f"Subject {sub} . Teacher name is {staff}")
#
# s = Stud("fgh",234567,"pune","python","jgf")


# class Qspiders:
#     def __init__(self,fee,branch,course):
#         self.fee = fee
#         self.course = course
#         self.branch = branch
#
# class Pyspiders(Qspiders):
#     def __init__(self,fee,branch,course,sub,framework):
#         super().__init__(fee, branch, course)
#         self.sub = sub
#         self.framework = framework
#
#     def details(self):
#         print(f"fee = {self.fee} course = {self.course} branch = {self.branch}")
#         print(f"sub = {self.sub} framework = {self.framework}")
#
# p = Pyspiders(32000,"Deccan","Java Full Stack", "Java", "springboot")
# p.details()
#
# print(Pyspiders.__mro__)

# __mro__   method resolution order
# print(class_mame.__mro__)

class X :
    c =10

class Y :
    a= 100
    b =190
    c=10

class Z (X,Y):
    a=100
    b=102
    c=900

z = Z()
print(z.a)
print(z.c)
print(z.b)





