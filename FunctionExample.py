# Function programs


# 1.wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference

def add_Sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


# a = int(input("Enter the 1st number : "))
# b = int(input("Enter the 2nd number : "))
#
# print(add_Sub(a,b))

# 2.waf to check string is palindrome or not (take user input)

def palindrome():
    string = eval(input("Enter the String : "))

    if string == string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} not a palindrome")


# palindrome()

# 3.wap to return length of variable keywords arguments

def length_keyword_agrs(**kwargs):
    return len(kwargs)


# print(length(a=1,b=2,c=4))

# 4.wap to return length of the variable positional arguments

def length_positional_agrs(*args):
    return len(args)

# print(length_positional_agrs(1,2,3,3,567))

# 5.wap to search for character in a given string and return corresponding index

def search_character(string, ch):
    if ch in string:
        return string.index(ch)
    else:
        print(f"{ch} is not present in the string")


# string = "coding part is done"
# ch = str(input("Enter the character : "))
# print(search_character(string, ch))

# 6.wap to squaring of the element in the given list
def square(l):
    for i in l:
        print(f"{i} = {i**2}")

# l = [1, 2, 3, 4, 5]
# square(l)

# 7.wap to fetch last digit number

def last_digit(num):
    return abs(num)%10


# num = int(input("Enter the number : "))
# print(last_digit(num))

# 8.wap to read 3 numbers from the user,first two numbers should be added and the result of
# addition should be subtracted by third number

# a = int(input("Enter the 1st number : "))
# b = int(input("Enter the 2nd number : "))
# c = int(input("Enter the 3nd number : "))

def add_sub(a,b,c):
    return (a+b)-c

# print(add_sub(a,b,c))

# 9.wap to find square,cube,square root and cube root of a number

def sqr(n):
    return n**2


def cube(n):
    return  n**3


def sqr_root(n):
    return n**0.5


def cube_root(n):
    return round(n**0.334,1)

# print(sqr(2))
# print(cube(2))
# print(sqr_root(4))
# print(cube_root(125))


# 10.wap to check the given characters is alphabets or digit or special characters

def check_character(ch):
    if "A"<=ch<="Z" or "a"<=ch<="z" :
        print(f"{ch} is a alphabet")
    elif "0" <=ch<="9":
        print(f"{ch} is a digit")
    else:
        print(f"{ch} is a special character")

# check_character(str(input("Enter the chacter : ")))

# 11.wap to check given iterable is a sequence,if it is a sequence reverse it,
# if not add one extra element to the iterable

def check_sequence(l):

    if isinstance(l,(str,list,tuple)):
        print(l[::-1])
    else:
        l["l"]="l"
        print(l)

# l = [1,2,3]
# check_sequence(l)

l = {"1":2,"l":"l"}
check_sequence(l)


# 12.write a function to print the below output
# func("TRACXN",1)
# #should print RCN
#
#
# 13.write a function to print the below output
# func("TRACXN",0)
# #should print TAX
#
#
# 14.A function take variable number of positional arguments as input. how to check if the arguments are more than 5.

def number_args(*args):
    if len(args)>5:
        print("Number of arguments are more than 5")
    else:
        print("Number of argument are less than 5")

# number_args(1,2,3,4,5)


# 15.WAF to reverse any iterable without using reverse function

def reverse_iterable(data):
    s = ""
    for i in data:
        s = i+s
    return s

# data = eval(input("Enter the data : "))
# print(reverse_iterable(data))

# 16.waf to return a dictionary with characters and ascii value pair

def char_ascii(data):
    d = {}
    if isinstance(data,(list,tuple,str)):
        for i in data:
            d[i]=ord(i)
    else:
        d[data]=ord(data)
    return d

# data = input("Enter the data : ")
# print(char_ascii(data))

# 17.waf to reverse a iterable if you are passing string or list or tuple else print type of the data

def reverse(value):
    if isinstance(value,(list,str,tuple)):
        print(value[::-1])
    else :
        print(type(value))

# value = eval(input("Enter the value : "))
# reverse(value)



# def re(str):
#     l = []
#     for i in str.split():
#         l.append(i)
#     return l
# str = "sasd asdf asdf asdfg"
# print(re(str))
#
# print(str.split())