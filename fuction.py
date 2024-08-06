# 1.Positional argument

# def info(name, email):
#     print(f"My name is {name} and my email is {email}")
# info("Dhanshri","d@gmail.com")

# 2. Keyword argument(=)

# def sum(a,b):
#     print(a+b)
# sum(a=10, b=10)

# 3. Only positional argument(/)

# def add(a,b,/,c):
#     print(a+b+c)
# add(1,2,3)
# add(1,2,c=3)
# add(a=1,3,4)

# 4. Only Keyword argument(*)

# def sum(*,a,b,c):
#     print(a+b+c)
# sum(a=1,b=2,c=3)

# 5.combination of positional and keyword argument(/,*)

# def sub(a,b,/,c,*,d):
#     print(a-b-c-d)
# sub(1,2,c=1,d=2)
# sub(a=1,b=3,1,d=0)
# sub(1,2,3,d=10)

# 6.variable positional argument(Give the answer in th tuple)

# def hi(*args):
#     print(args)
# hi(1,2,3,4,5)

# def hi(*args):
#     print(*args)
# hi(1,2,3,4,5)

# 7. Variable keyword argument(Give the answer in dictionary)

# def div(**kwargs):
#     print(kwargs)
# div(a=1,b=2)

# 8.Combination of the (*,**)

# def comb(*args,**kwargs):
#     print(args,kwargs)
# comb(1,2,3,4,a=1,b=2,v=3)

# Default argument

# def sum(a=0,b=0,c=0):
#     print(a+b+c)
# sum(1,2,3)
# sum()
# sum(1,2)
# sum(1)


