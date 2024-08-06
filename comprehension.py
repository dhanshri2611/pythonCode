# List Comprehension

# 1. whenever we have only for loop condition

# var_name=[expression for loop condition]

# 2. whenever we have only if condition

# var_name=[expression for loop condition if condition]

# 3. whenever we have both if and else condition

# var_name=[expression if condition else block for loop condition]


# Dict Comprehension

# 1. whenever we have only for loop condition

# var_name={key:value for loop condition}

# 2. whenever we have only if condition

# var_name={key:value for loop condition if condition}

# 3. whenever we have both if and else condition

# var_name={key:value if condition else block for loop condition}

# Set Comprehension

# 1. whenever we have only for loop condition

# var_name={expression for loop condition}

# 2. whenever we have only if condition

# var_name={expression for loop condition if condition}

# 3. whenever we have both if and else condition

# var_name={expression if condition else block for loop condition}
# a=[1,2,3,4,5,6]
# x=[i for i in a]
# print(x)

# print([i**2 if i%2==0  else i**3 for i in a])

# square only odd num
# print([i**2 for i in a if i%2==1])

# Set Comprehension
# print({i**2 if i%2==0  else i**3 for i in a})
#
# print({i**2 for i in a if i%2==1})
#
# print({i for i in a})


# dict

# a = [10, 20, 35, 45, 75]
# d={}
# for i in a:
#     if i %2 ==0:
#         d[i]=i**2
#     else:
#         d[i]=i**3
#
# print(d)

# print({i: i ** 2 if i % 2 == 0 else i ** 3 for i in a})


# a = [1, 2, 34]
#
# print((i for i in a))  #generator object address
# print(list(i for i in a))  #type cast


s = "Good Morning"

print([i  for i in s])