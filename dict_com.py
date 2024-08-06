# Dict comprehensions
#
# 1.wap to create a dictionary keys by taking from list,values are square of that key
#
# l=[2,3,4,1,6,2,7,8,4]
# print({i:i**2 for i in l})
#
# 2.wap to create a dictionary of values and index pair
#
# l=["google","apple","python","orange"]
# #
# print({l[i]:i for i in range(0,len(l),1)})
# #
# 3.wap create a dictionary having first char of word and word pair if word having even length
#
# l=["google","apple","python","orange"]
# print({i[0]:i for i in l if len(i)%2==0})
#
#
# 4.wap to check length of words and create a dict having word and word pair if it is even odd as it is else reverse and add
#
# l=["google","apple","python","orange"]
# #
# print({i[0]:i[::-1] if len(i)%2==1 else i for i in l })

#
# 5.wap to check elements is palindrome key and value should be same else value is reverse of key
#
# l=["banana","malayalam","madam","sir","mom","dad"]
# print({i:i if i==i[::-1] else i[::-1] for i in l })
#

# set-----------------
# 1.wap to remove repeated values and return in set
# l=[2,3,4,2,5,6,2,3]
#
# print({i for i in set(l)})
# #
# # 2.wap to take two lists and return a set by adding elements present same index
# #
# l1=[2,3,4,5,6,7,8,9]
# l2=[5,6,7,8,9,1,2,3]
#
# print({sum(i) for i in zip(l1,l2)})

