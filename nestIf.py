#check the given number is string and palindrome or not

# data = eval(input("Enter the data : "))
# if isinstance(data,str):
#     print("It's a string")
#     if data[::-1]==data:
#         print("it's palindrome")
#     else :
#         print("its not palindrome")
# else :
#     print("it's  not a string")

#2.wap to check the number is odd and check if the number is divisible by 7
# n=35
# if n%2!=0 :
#     print("It's odd")
#     if n%7==0:
#         print("it's divisible by 7")
#     else :
#         print("it is not divisible")
# else :
#     print("It's not odd number")

# 3.wap to check the number is odd and check if the number is divisible by 7
# n=33
# if n%2!=0 :
#     print("It's odd")
#     if n%7==0:
#         print("it's divisible by 7")
#     else :
#         print("it is not divisible by 7")
# else :
#     print("It's not odd number")

# 4.wap to validate facebook username and password
# condition is:---> username-->"python"  and password="python masters"
# username = "python"
# password = "python masters"
#
# un = eval(input("Enter the Username : "))
# pwd = eval(input("Enter the password : "))
#
# if un==username :
#     if pwd==password:
#         print("login success!!")
#     else :
#         print("Please Enter valid password")
# else:
#     print("Please enter valid username")


# 5.wap to Book ticket in Book my show
# condition:---> first it should ask theaters name then it should display the movie available then it has to display ticket price and in the end ticket should be booked

# theater_name = ["maratha tockies", "xyz", "ABC"]
# print(theater_name)
# user = eval(input("Enter the theater name : "))
# if user in theater_name :
#     print(f"you choose the {user} theater")
#     movies = ["abc","xyz","pqr"]
#     print(f"available movies are {movies}")
#     user1 = eval(input("Enter the movie : "))
#     if user1 in movies :
#         price = [500,200,1000]
#         # if user1 == movies[0] :
#         #     print(f"Pay {price[0]}")
#         # elif user1 == movies[1] :
#         #     print(f"Pay {price[1]}")
#         # elif user1 == movies[2] :
#         #     print(f"Pay {price[2]}")
#         # else:
#         #     print("please the valid amount!!")
#
#         amount = eval(input("Enter the amount : "))
#
#         if amount==price[0] or movies[0]==user1 :
#             print(f"you booked {user1}")
#         elif amount==price[1] or movies[1]==user1:
#             print(f"you booked {user1}")
#         elif amount==price[2] or movies[2]==user1:
#             print(f"you booked {user1}")
#         else:
#             print("please the valid amount!!")
#
#     else:
#         print("Plese choose the movies from which are dieplayed!!")
# else:
#     print("please enter the theater which are present in the theater!!")


# 6.wap to find middle element is even or odd
# s=[3,4,6,7,9,1,5,8]
# if len(s)%2==1:
#     res = len(s)//2
#
#     if res%2==0:
#         print("It is even")
#     else:
#         print("it is odd")
# else:
#     print("length is even")

#wap to purches the phone in flipcard or amazon

# app =["Flipkart","Amazon"]
# print(app)
# user = input("Choose the app : ")
# if user in app:
#     phone =["Redmi","Vivo","1+"]
#     print(phone)
#     user1 = input("Choose the phone : ")
#     if user1 in phone:
#         price = [10000,20000,30000]
#
#         pos= phone.index(user1)
#         print(f"{user1} : {price[pos]}")
#         amount = int(input("Enter the amount : "))
#         if amount == price[0] and user1 == phone[0]:
#             print(f"You buy the {phone[0]} ")
#         elif amount == price[1] and user1 == phone[1]:
#             print(f"You buy the {phone[1]} ")
#         elif amount == price[2] and user1 == phone[2]:
#             print(f"You buy the {phone[2]} ")
#         else:
#             print("Enter valid amount : ")
#     else:
#         print("Phone not available")
# else:
#     print("Choose correct app")


app=["flipkart","Amezon"]
userApp=input(f"{app} choose app")

if userApp in app:
    mobile=["vivo","oppo","samsung","iphone"]
    userMobile=input(f"{mobile} choose the mobile")
    if userMobile in mobile:
        print(f"{userMobile} selected" )
        if userMobile=="vivo":
            vivo={"v1":20000, "vivo x1":40000, "vivo y35":18000}
            model= (input(f"{vivo} select model"))
            price=vivo.get(model)
            userPrice=int(input(f"your price is {price} pay the amount!"))
            if userPrice==price:
                print("mobile booked")
            else:
                print("invalid amount")
        if userMobile == "oppo":
            oppo = {"f1": 20000, "reno": 40000, "f2": 18000}
            model = (input(f"{oppo} select model"))
            price = oppo.get(model)
            userPrice = int(input(f"your price is {price} pay the amount!"))
            if userPrice == price:
                print("mobile booked")
            else:
                print("invalid amount")
        if userMobile == "samsung":
            samsung = {"s23": 80000, "A53 ": 40000, "note 2.": 50000}
            model = (input(f"{samsung} select model"))
            price = samsung.get(model)
            userPrice = int(input(f"your price is {price} pay the amount!"))
            if userPrice == price:
                print("mobile booked")
            else:
                print("invalid amount")
        if userMobile == "iphone":
            iphone = {"iphone11": 20000, "iphone 12": 40000, "iphone13": 18000}
            model = (input(f"{iphone} select model"))
            price = iphone.get(model)
            userPrice = int(input(f"your price is {price} pay the amount!"))
            if userPrice == price:
                print("mobile booked")
            else:
                print("invalid amount")

    else:
        print("mobile not found")

else:
    print("choose valid app")
