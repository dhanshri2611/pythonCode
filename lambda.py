# Annonymous Function/ Lambda Function

# without calling function execute the function

# syntax ----------->  lambda arg1,arg2,....:expresion

# m = lambda z : f"{z} is even" if z%2==0 else f"{z} is odd"
# print(m(2))

# s = "level"
#
# pal = lambda s : f"{s} is palindrome" if s==s[::-1] else f"{s} is not palindrome"
# print(pal(s))



# 1.wap to find square and cube of given number

# square = lambda num : f"{num} square is {num**2} and {num} cube is {num**3}  "
# print(square(2))

# 2.wap to check the given number is palindrome or not

# pal = lambda s : f"{s} is palindrome" if s==s[::-1] else f"{s} is not palindrome"
# print(pal("1211"))

# 3.wap to convert negative number to positive number

# neg_to_pos = lambda a : abs(a)
# print(neg_to_pos(-1))

# 4.wap to return the key of a dictionary
# a={"hello":"Sony","How":"are","you":"bye"}
#
# k =lambda a : a.keys()
# print(k(a))

# print(lambda a : a.keys())

# 5.wap to check if the number is even or odd

# m = lambda z : f"{z} is even" if z%2==0 else f"{z} is odd"
# print(m(2))

# 6.wap which returns first element of a sequence

# ele = lambda l : l[0] if isinstance(l,(str,list,tuple)) else f"{l} not a sequence"
# print(ele(1))

# 7.wap which returns length of any iterable

# length = lambda s : len(s) if isinstance(s,(list,set,str,tuple)) else f"{s} is not a iterable"
# print(length([1,3,4]))

# 8.wap which returns the list of squares of numbers in a list
# l=[2,3,4,5,6]
# sq = lambda l : list(i**2 for i in l)
# print(sq(l))

# 9.wap to check list elements are palindrome or not

# l=["nayana","kayak","mom","school","bag","dad"]
# z = lambda l : list("is palindrome" if i == i[::-1] else "Not plaindrome" for i in l)
# print(z(l))

# 10.wap to print the numbers present in a list with their corresponding indices pair

# l=[100,200,300,400,500]
#
# i = lambda l:list(enumerate(l))
# print(i(l))

# i = lambda l : list(f"{i} ---> {l.index(i)} " for i in l)
# print(i(l))

# 11.wap to check a data is sequence if it is sequence then return length pair else type pair

# data = lambda l: (f"{len(l)}" if isinstance(l,(str,tuple,list)) else f"{type(l)}")
# print(data((1,23)))

# 12.wap to check given number is divisible by 5 and 3


# num = lambda num: f"{num} is divisible by 5" if num%5==0 and num%3==0 else "Not divisible by 5 and 3"
# print(num(25))

# 13.wap to check even or odd,if it is even return square of that value else square root of that
# value

# even_odd = lambda i : i**2 if i%2==0 else i**0.5
# print(even_odd(9))

# 14.wap to check len of given string ,if length is even return as it is else return reverse
# of that string

# length = lambda string : len(string) if len(string)%2==0 else string[::-1]
# print(length("sdfghj"))

# 15.wap to check length of given string and return value and length in tuple and dictionary

# ans=lambda s:[(s,len(s)),{s:len(s)}]
# print(ans("Sky"))