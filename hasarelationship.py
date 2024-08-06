# class Pendrive:
#     def insert(self):
#         print("pendrive inserted")
#
#
# class Laptop:
#     name = "hp"
#     price = 47000
#
#     def details(self):
#         print(f"Laptop name is {self.name} and price is {self.price}")
#         pendrive = Pendrive()
#         pendrive.insert()
#
# l = Laptop()
# l.details()


# using constructor

# class Employee:
#     empid = 101
#     def __init__(self,name):
#         print(f"Employee name is {name}")
#
# class Employee_sal:
#     def __init__(self,sal):
#         print(f"Salary is {sal}")
#         self.x = Employee("Dhana")
#         print(self.x.empid)
#
# emp = Employee_sal(56789)


# method overloading

# class Arithmetic:
#     def add(self,a,b):
#         print(a+b)
#
#     def add(self,a,b):
#         print(a-b)
#
# a = Arithmetic()
# a.add(10,20)
