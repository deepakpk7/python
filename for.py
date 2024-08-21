# 1-10 Numbers print

# for i in range(11):
#     print(i)
# print("*******************")
# for i in range(2,11):
#     print(i)
# print("*******************")
# for i in range(2,21,2):
#     print(i)
# print("*******************")

# # SUM OF NUMBERS

# s=int(input("Enter the starting no : "))
# e=int(input("Enter ending no :"))
# sum=0
# for i in range(s,e+1):
#     print(i)
#     sum+=i
# print("Number of Sum= ",sum)

# Sum of Even Numbers

# s=int(input("Enter the starting no : "))
# e=int(input("Enter ending no :"))
# sum=0
# for i in range(s,e+1):
#     if i%2==0:
#         print(i)
#         sum+=i
# print("Sum of Even No = ",sum)

# MULTIPLICATION TABLE

# m=int(input("Enter a multiplication :"))
# l=int(input("Last value"))
# i=0
# for i in range(i,l+1,i+1):
#     print(i,"*",m,"=",i*m)

# SUM OF NUMBERS

# f=int(input("Enter a first no : "))
# l=int(input("Enter a last number : "))
# i=0
# sum=0
# sum1=0
# sum2=0
# for i in range(f,l+1):
#     sum=sum+i
#     if i%2==0:     
#         sum1=sum1+i
#     else :
#         sum2=sum2+i
#     i+=1
# print("Sum of Numbers =",sum)
# print("Sum of Even  Numbers =",sum1)
# print("Sum of Odd  Numbers =",sum2)

# FACTORIAL OF A NUMBER

# a=int(input("Enter a number : "))
# i=1
# f=1
# for i in range(i,a+1):
#     f*=i
# print("Factorial of number : ",f)

# REVERSE A NUMBER

# n=int(input("Enter a no :: "))
# r=0
# for i in range(n,n+1):
#     d=n%10
#     r=r*10+d
#     n//=10
# print("Reverse = ",r)

# SUM OF A DIGIT

# n=int(input("Enter a no :: "))
# s=0
# for i in range(n):
#     s+=i
# print("Sum of digit =",s)   

# String

# s=input("Enter a string : ")
# i=0
# for i in s:
#     print(i)

# STRING REVERSE

s=input("Enter a string : ")
r=''
for i in s:
    r=i+r 
print("Reverse a String :",r)
