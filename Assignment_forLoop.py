# Assignment questions:--->
#
# 1.WAP to extract & store the extensions of files in a list
# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx','lambda.png', 'map.py', 'python.pdf', 'oops.py']
# li = []
# for i in l:
#     a=i.split(".")
#     li+=[a[1]]

#     li.append(i.split(".")[1])
# print(li)

# 2.wap to print first and last char of each name in the list
# l = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]
# l1 = []
# for i in l:
#     l1.append(i[0])
#     l1.append(i[-1])
# print(l1)

# 3.wap to create new list as squares of each number of below list
# l = [2, 4, 5, 1, 9, 7, 3]
# sq = []
# for i in l:
#     sq.append(i**2)
# print(sq)

# 4.wap if number is even the print its square else print its cube
# l = [2, 4, 5, 1, 9, 7, 3]
# for i in l:
#     if i%2==0:
#         print(i**2)
#     else:
#         print(i**3)

# 5.wap to create a new list of separate even number and odd number

# l = [2, 4, 5, 1, 9, 7, 3]
# l1 = []
# for i in l:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l1.insert(0,i)
# print(l1)

# 6.wap to create a new list reversing each name from the list.
# names = ["Sunil", "denga", "panga", "Harsha", "manga"]
# l = []
# for i in names:
#     l.append(i[::-1])
# print(l)

# 7. WAP  to find the number of digits present in a number
# n = 123456
# print(len(str(n)))

# 8.WAP to print largest number in the list without using inbuilt function

# numbers = [10, 30, 50, 80, 15, 20, 70,25]
# num = 0
# for i in numbers:
#     if num<i:
#         num = i
# print(num)

# 9.WAP to print all numeric values in a list
# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],True, (1,3,7), 6+3j]
# l1 = []
# for i in l:
#     if isinstance(i,(float,int,complex,bool)):
#         l1.append(i)
# print(l1)

# 10.WAP to perform copy method in a list without using copy()(take user input)
# l = list(input("Enter the numbers : "))
# l1 = []
# for i in l:
#     l1.append(i)
# print(l1)

# 11.WAP to check the given number is Armstrong or not
# Armstrong : Sum of cube of the digits
# num=370
# sum = 0
# l = str(num)
# for i in l:
#     sum =sum+(int(i)**len(l))
# if sum == num:
#     print("its armstrong")
# else:
#     print("It not armstrong")

# 12.WAP to check given number is perfect number or not(take user input)
# sum of its proper divisor should be equal to original value
# num = int(input("Enter the number : "))
# sum = 0
# for i in range(1,num):
#    if num % i == 0:
#        sum+=i
# if sum == num:
#     print("It is a perfect number")
# else:
#     print("It not a perfect number")


# 13.WAP to print Fibonacci numbers up to 10
# n = 0
# n1 = 1
# res = 0
# for i in range(10):
#    print(n,end=" ")
#    res = n+n1
#    n = n1
#    n1 = res

# fibo = [0,1]
# n = int(input("Enter the number: "))
# for i in range(2,n):
#    fibo.append(fibo[-1]+fibo[-2])
#
# print(fibo)

# 14.WAP to check given number is Automorphic or not
# automorphic means:-->square end with the integer
# l = [1,5,6,25,76,376,625,9376,2]
# for i in l:
#     if str(i**2).endswith(str(i)):
#         print(f"{i} automorphic")
#     else:
#         print(f"{i} not automorphic")

# 15. WAP to reverse each element in a list, then reverse entire list

# names = ['apple', 'google', 'yahoo', 'Walmart']
# l1 = []
# for i in names:
#     l1.append(i[::-1])
# print(list(reversed(l1)))



