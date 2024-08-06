# 1. Default except block

# l = [1,2,3,4]
# try :
#     print(l[10])
# except :
#     print("Erroe is handled!!")

# 2. Specific except block

# a = 10
# b = 0
# print(a/b)

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Error handled!!")

# 3. Multiple except block

# a = 'hello'
# try :
#     print(a.values())
# except NameError:
#     print("name erroe is handled!!")
# except ValueError:
#     print("value error is handled!!")
# except AttributeError:
#     print("error handled!!")

# s = [1,2,3,4]
# try:
#     print(s.index(90))
# except (NameError, ValueError, AttributeError):
#     print("error handled!!")

# 5. Generic except block

a = 10
b = 0
try:
    print(a/b)
except Exception as err:
    print(err)