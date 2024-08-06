# odd length

# x = ["virat","king","vinya","sindhu","rohit"]
#
def odd_length(x):
    for i in x:
        if len(i)%2!=0:
            yield i
#
# print(list(odd_length(x)))

# wap to generate a+b,a-b,a*b,a/b by taking a and b from user

def arithmetic_operation(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b

# a = int(input("Enter the Number : "))
# b = int(input("ENter the number : "))
# print(list(arithmetic_operation(a,b)))


# wap to generate only values which are divisible by 5

# l=[34,55,60,56,78,90,25,40]

def divisible(l):
    for i in l:
        if i%5==0:
            yield i

# print(list(divisible(l)))


# wap to return a iterator which is having square root of values present in the list

# l=[25,36,49,81,9,16]

def square_root(l):
    for i in l:
        yield i**0.5

# print(list(square_root(l)))

# wap to return a iterator having tuples of word and its len pair and typecast into dictionary

# l=["instagram","facebook","whatsapp","meta","oracle"]

def word_iterator(l):
    for i in l:
        yield i, len(i)

# print(dict(word_iterator(l)))

# wap to generate only numeric values in given list

# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

def numeric_value(l):
    for i in l:
        if isinstance(i, (int,float,bool,complex)):
            yield i

# print(list(numeric_value(l)))

# wap to generate a list if it is individual data type reverse it else return as it is

# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
#
# def individual(l):
#     for i in l:
#         if isinstance(i,(int,float,bool,complex)):
#             i= str(i)[::-1]
#             yield eval(i)
#         else:
#             yield i
#
# print(list(individual(l)))


# wap to generate only the string with odd length in given list
#
# l=["alexa","siri","google","cortrena"]
# def oddLength(l):
#     for i in l:
#         if len(i)%2==1:
#             yield i
#
# print(list(oddLength(l)))



#
#
# wap to create a list of numbers if number are even square it else cube it
# l=[2,3,4,5,6,7]
# def evenSq(l):
#     for i in l:
#         if (i)%2==0:
#             yield i**2
#         else:
#             yield i**3
# print(list(evenSq(l)))
#
# wap to return a list if words is of even length reverse it
#
l=["hello","world","python","apple","google","walmart"]
#
# def rev(l):
#     for i in l:
#         if len(i)%2==0:
#             yield i[::-1]
# print(list(rev(l)))
#
# wap to generate the first letter of the word as key and words starting with letter as value
s="python is a programming language and programming is part of life"
def dic(s):
    d={}
    for i in s.split():
        if i[0] in d:
            d[i[0]]+=[i]
        else:
            d[i[0]]=[i]
    yield d

print(list(dic(s)))

# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]

