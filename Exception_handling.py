# a='welcome'
# b='10'
# try:
#     print(a+b)
# except:
#     pass
# else:
#     print("Error is except not work")
# finally:
#     print("Always print")

# def number():
#     a=int(input("Enter a number :"))
#     b=int(input("Enter a number :"))
#     return a,b

# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# div=lambda a,b:a/b
# mul=lambda a,b:a*b
# mod=lambda a,b:a%b

# while True:
#     print('''
#         1.addition
#         2.substraction
#         3.division
#         4.mulitiplication
#         5.modulous
#         6.exit''')
#     while True:
#         try:
#             choice=int(input('enter the choice: '))
#             break
#         except:
#             print("******To enter valid choices*****")
#     if choice==1:
#         a,b=number()
#         print(add(a,b))
#     elif choice==2:
#         a,b=number()
#         print(sub(a,b))
#     elif choice==3:
#         a,b=number()
#         print(div(a,b))
#     elif choice==4:
#         a,b=number()
#         print(mul(a,b))
#     elif choice==5:
#         a,b=number()
#         print(mod(a,b))
#     elif choice==6:
#         break
#     else:
#         print('invalid option')

l=[1,2,3,'s',4,5.1]
s=0
for i in l:
    if type(i)==int or type(i)==float:
        s+=i
# for i in l:
#     try:
#         s+=i
#     except:
#         pass
print(s)