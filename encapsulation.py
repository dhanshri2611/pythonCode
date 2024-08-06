# Encapsulation
# Wrapping a data into the single unit

# Access Specifier
# 1.public--->not prefixed with any symbol

# 2. protect-----> prefixed with '_'

# 3. private -----> prefixed with '__'


# 1.public access modifier

# class Emp:
#     empid = 101
#     def emp_details(self,name):
#         print(f"Emp name is {name}")
#         print(f"Emp id is {self.empid}")
#
# e = Emp()
# print(e.empid)
# e.empid= 102
# e.emp_details("dhana")

# class Emp:
#     empid= 101
#     def __init__(self,name):
#         self.name = name
#
#     def spam(self):
#         print(f"{self.name}")
#
# e = Emp("Dhana")
# print(e.name)
# e.name = "gk"
# print(e.name)

# 2. protected

# class Bank:
#     _pin = 1234
#     def _bank(self,name):
#         print(f"Bank name is {name}")
#         print(f"pin is {self._pin}")
#
# b = Bank()
# print(b._pin)
# b._bank("SBI")

# class Bank:
#     def __init__(self,name):
#         self._name = name
#
#     def _spam(self):
#         print(f"Bank name is {self._name}")
#
# b = Bank("SBI")
# b._spam()

# 3. private

# class Student:
#     __college = "SGMCOE"
#     def __details(self,name,rollno):
#         print(f"Student name is {name} and his roll no. is {rollno}")
#         print(f"College name is {self.__college}")
#
# s = Student()
# s._Student__details("dhana",63)
# print(Student._Student__college)
#
# print(Student.__dict__)
#
# class Student:
#     def __init__(self,name):
#         self.__name = name
#
#     def getter(self):
#         print("Getting the value")
#         return self.__name
#
#     def setter(self,name):
#         print("Setting the value")
#         self.__name = name
#
#     def delter(self,name):
#         print("Deleting the value")
#         del self.__name
#
# s = Student("Dhana")
# print(s.getter())
# s.setter("Gk")
# print(Student.__dict__)
# print(s._Student__name)
# s.delter("Gk")

# Accessing one class to another class protected variable
# class Bank:
#     _a = 10
#     def value(self):
#         print(self._a)
#
# class BankC(Bank):
#     def get_value(self):
#         print(f"{self._a}")
#
# b = BankC()
# b.get_value()

# class Bank:
#     __a = 10
#     def value(self):
#         print(self.__a)
#
# class BankC(Bank):
#     def get_value(self):
#         print(f"{self.__a}")
#
# b = BankC()
# b.get_value()

# class A :
#     _name = "Java"
#     def test(self):
#         print(f"{self._name}")
#
# class B(A):
#     _name = "Python"
#     def test1(self):
#         print(f"{super()._name}")
#
# b = B()
# b.test()
# b.test1()



