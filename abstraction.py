# Abstraction

# step 1.
# from abc import ABC, abstractmethod

# Abstract class

# from abc import ABC,abstractmethod
# class Sample(ABC):
#     @abstractmethod
#     def demo(self):
#         ...
#
# s = Sample()  # We can't create the object of the abstract class

# Abstract method

# from abc import ABC, abstractmethod
# class Sample:
#     @abstractmethod
#     def demo(self):
#         pass
#
# s = Sample()
# s.demo()

# Concreate Class

# class Sample:
#     def demo(self):   #declaration
#         print("From demo method")    #defination
#
#     def demo2(self):
#         print("From demo2")
#
# s = Sample()
# s.demo()
# s.demo2()

# Concreate method

# def demo(self):   #declaration
#         print("From demo method")    #defination

# Bank Ex


# from abc import ABC, abstractmethod
#
# class Bank(ABC):
#     @abstractmethod
#     def bank_name(self,name):
#         pass
#
#     @abstractmethod
#     def deposit(self, amount):
#         ...
#
# class BankImpli(Bank):
#     def bank_name(self,name):
#         print(f"My bank name is {name}")
#
#     def deposit(self, amount):
#         print(f"My deposit amount is {amount}")
#
# b = BankImpli()
# b.bank_name("HDFC")
# b.deposit(20000)

# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def bank(self):
#         ...
#
#     @abstractmethod
#     def deposit(self,amount):
#         ...
#
#     @abstractmethod
#     def withdraw(self,amount):
#         ...
#
# class Bank_Impli(Bank):
#     def __init__(self, bal):
#         self.bal = bal
#
#     def bank(self):
#         print("my bank name is HDFC")
#
#     def deposit(self,amount):
#         print(f"Before deposit my balance is {self.bal}")
#         self.bal+=amount
#         print(f"After depositing my balance is {self.bal}")
#
#     def withdraw(self,amount):
#         print(f"My balance is {self.bal}")
#         self.bal-=amount
#         print(f"After withdrawal balance is {self.bal}")
#
#
# b = Bank_Impli(99999)
# b.bank()
# b.deposit(1)
# b.withdraw(99999)


# WhatsApp EX

# from abc import ABC,abstractmethod
#
# class WhatsApp(ABC):
#     @abstractmethod
#     def updates(self,story):
#         ...
#
#     @abstractmethod
#     def calls(self,phone):
#         ...
#
#     @abstractmethod
#     def community(self,community_name):
#         ...
#
#     @abstractmethod
#     def chats(self,name,msg):
#         ...
#
#     @abstractmethod
#     def settings(self):
#         ...
#
# class WhatsApp_impli(WhatsApp):
#
#     def __init__(self):
#     def updates(self,story):
#         print(f"Story updated {story}")
#
#     def calls(self,phone):
#         print(f"calling to the {phone}")
#
#     def chats(self,name,msg):
#         print(f"Msg sent to the {name}")
#         print(f"and your msg is {msg}")
#
#     def community(self,community_name):
#         print(f"you search {community_name}")
#         print("If you join this community click on join")
#
#     def settings(self):
#         print("Setting updated")
#
# w = WhatsApp_impli()
# w.calls("7447899709")
# w.chats("dhana","Hii")
# w.updates(2)
# w.community("GK")
# w.settings()

# from abc import ABC,abstractmethod
#
# class BookMyShow(ABC):
#     @abstractmethod
#     def theater_name(self, name):
#         ...
#
#     @abstractmethod
#     def movie_name(self,movie_name):
#         ...

#     @abstractmethod
#     def price(self,amount):
#         ...
#
#     @abstractmethod
#     def seat(self,seat):
#         ...
#
# class BookMyShow_Impli(BookMyShow):
#     def __init__(self,theater_name,movie_name,price,seat):
#         self.theater_name = theater_name
#         self.movie_name = movie_name
        self.price = price
        self.seat = seat

    def theater_name(self, name):
        if(self.theater_name == name):
            print(f"You select theater name is {name}")
        else:
            print("not present")

    def movie_name(self,movie_name):
        if(self.movie_name == movie_name):
            print("Movie is available if you want book then click yes")
#         else:
#             print("not available")
#
#     def price(self,amount):
#         if(self.amount)
#
#
# b = BookMyShow_Impli("XYZ","Munja",[100,200,300],[1,2,3])
#
# b.theater_name("abc")






