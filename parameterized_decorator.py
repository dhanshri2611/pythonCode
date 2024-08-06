# parameterized decorator

# def outer_most(parameter):
#     def outer(func):
#         def inner(*a,**k):
#             stmt
#             func(*a,**k)
#         return inner
#     return outer
#
# @outer_most
# def main_fuction():
#     print()
# main_fuction()

# def outer_most(x):
#     def outer(func):
#         def inner(*a,**k):
#             print(x)
#             func(*a,**k)
#         return inner
#     return outer
# @outer_most("Hey guys")
# def great():
#     print("Good morning")
# great()

import time
def outer_most(n):
    def outer(func):
        def inner(*a,**k):
            time.sleep(n)
            print(n)
            func(*a,**k)
        return inner
    return outer

@outer_most(2)
def add():
    print("Add method")
add()

@outer_most(5)
def funny():
    print("Funny method")
funny()

@outer_most(3)
def magic():
    print("Magic method")
magic()