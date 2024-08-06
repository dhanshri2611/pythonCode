# Decorator

# def outer(fuc):
#     def inner(*args,**kwargs):
#         statment
#         fuc(*args,**kwargs)
#     return inner
# @outer
# def main_func(parameter):
#     statement
# main_func()

#   Decorators Examples

# 1.write a decorator function that prints "HELLO EVERYONE" message before execute any function

# def outer(add):
#     def inner(a,b):
#         print("HELLO EVERYONE")
#         add(a,b)
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# add(5,7)

# 2.write a decorator function to print main function name before executing any decorator function

# def outer(multi):
#     def inner(a,b):
#         print(multi.__name__)
#         multi(a,b)
#     return inner
# @outer
# def multiplication(a,b):
#     print(a*b)
# multiplication(2,4)

# 3.write a decorator which inputs 5 seconds of delay before executing any decorator function

import time
# def outer(info):
#     def inner():
#         # info()
#         time.sleep(1)
#         info()
#         print(f"My name is : {input()}")
#
#     return inner
# @outer
# def info():
#     print("Hello")
#
# info()






# import time
# def outer(func):
#     def inner():
#         user_input = eval(input("enter the value"))
#         # print(f'{user_input}')
#         func()
#         time.sleep(3)
#         print(f"my name is {user_input}")
#     return inner
#
# @outer
# def Hi():
#     print("hello")
#
# Hi()


# 4.write a decorator function calculate the execution time of any function

# import time


# def outer(add):
#     def inner(a, b):
#         start = time.time()
#         print(f"Addition of {a}+{b} is")
#         add(a, b)
#         end = time.time()
#         print(end - start)
#
#     return inner
#
#
# @outer
# def add(a, b):
#     print(a + b)
#
#
# add(3, 5)

# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the original function

# def outer(div):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#             return div(a, b)
#
#     return inner
#
#
# @outer
# def divison(a, b):
#     print(a / b)
#
#
# divison(2, 4)

# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"
#
# o/p--->"i am doing addition operation"
#        value
#      "addition operation is done

# def outer(add):
#     def inner(a,b):
#         print("i am doing addition operation")
#         add(a,b)
#         print("addition operation done")
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# add(5,7)

# 7.create a decorator to return only positive out from any subtraction

# def outer(sub):
#     def inner(a,b):
#         res=sub(a,b)
#         print(abs(res))
#     return inner
# @outer
# def sub(a,b):
#     return a-b
# sub(69,45)

# 8.create a decorator which counts the number of function calls
#
# ct=0
# def outer(f):
#     def inner():
#         global ct
#         ct+=1
#         f()
#     return inner
# @outer
# def greet():
#     print("good morning")
# greet()
# greet()
# greet()
# greet()
# print(ct)

# 9.wap to sum of the positional arguments and get the length of the keywords arguments
# def out(func):
#     def inn(*args,**kwargs):
#        print(sum(args))
#        print(len(kwargs))
#        func(*args,**kwargs)
#     return inn
# @out
# def add(*args,**kwargs):
#     return args,kwargs
# add(1,3,4,a=2,d=0)

# 10.write a decorator function to print the type of datatype before performing the action

# def out(t):
#     def inn(*args):
#         for i in args:
#             print(f"type of {i} is {type(i)}" )
#
#     return inn
# @out
# def t(*args):
#     print(args)
# t(22,145,22.0,True,4+5j)

# 11.write a decorator operation on the given number and the condition is A>B then perform multiplication in decorator function else
#  cube it in decorator

# def outer(multi_cube):
#     def inner(a,b):
#         if a>b:
#             print(a*b)
#         else:
#             print(a**3)
#             print(b**3)
#         multi_cube(a,b)
#     return inner
# @outer
# def multi_cube(a,b):
#     return a,b
#
# multi_cube(9,3)


# 12.create a decorators to which prints name of called main function and counts the function calls

# count = 0
# def outer(name):
#     def inner():
#         print(name.__name__)
#         global count
#         count+=1
#         name()
#     return inner
# @outer
# def name():
#     print(f"{count} this time the function is call")
# name()

# 13.create a decorators to which prints names of called functions and checks the number is even or odd

# def outer(name):
#     def inner(num):
#         print(f"Calling function name is : {name.__name__}")
#         if num % 2 == 0:
#             print(f"{num} Its even")
#         else:
#             print(f"{num} is odd")
#         name(num)
#     return inner
# @outer
# def check_num(num):
#     return num
# check_num(int(input("Enter the number : ")))

# 14.create a decorator which delays its execution as per user input

# import time
# def outer(delay):
#     def inner(delay_time):
#         print("Hello")
#         time.sleep(delay_time)
#         print("Hello")
#         delay(delay_time)
#     return inner
# @outer
# def delay(time):
#     return time
# delay(int(input("Enter the time: ")))

# 15.write a multilevel decorator to log some message

# def outer(add):
#     def inner(a,b):
#         add(a,b)
#         print("We use addition operator")
#     return inner
#
# def outer1(add):
#     def inner2(a,b):
#         print(f"Addition of {a}+{b}")
#         add(a,b)
#     return inner2
#
# @outer1
# @outer
# def add(a,b):
#     print(a+b)
# add(1,2)


# 16.write a multilevel decorators to accept username and register number of employee

# def username(emp):
#     def inner(*args,**kwargs):
#         print(un)
#         emp(*args,**kwargs)
#     return inner
#
# def password(emp):
#     def inner1(*args,**kwargs):
#         print(pwd)
#         emp(*args,**kwargs)
#     return inner1
#
# un = eval(input("Enter the username : "))
# pwd = eval(input("Enter the password : "))
# @username
# @password
# def emp(un,pwd):
#     return un,pwd
#
# emp(un,pwd)









# def log(func):
#     def inner(*args,**kwargs):
#         print("i am logging")
#         func(*args,**kwargs)
#     return inner
#
# def register(func):
#     def wrapper(*args,**kwargs):
#         print("i have registered")
#         func(*args,**kwargs)
#     return wrapper
# @log
# @register
#
# def Employee(name,reg):
#     print(name,reg)
# name=eval(input("pass name:"))
# reg=eval(input("pass email id"))
#
# Employee(name,reg)

