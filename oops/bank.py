# class Bank:
#     def __init__(self,min):
#         self.bal=min
#     def deposit(self,amt):
#         self.bal+=amt
#         print("Deposited...",amt)
#     def windrow(self,amt):
#         self.bal-=amt
#         print("Windrow...",amt)
#     def display(self):
#         print("Balances= ",self.bal)
    
# user1=Bank(100)
# print("Current Balances:",user1.bal)
# user1.deposit(10)
# user1.windrow(7)
# user1.display()

# class Demo:
#     def __init__(self,a):
#         print(a)
# ob=Demo(12)

class Demo:
    def __init__(self,name,age):
        print(name,age)
a=Demo('deepak',21)