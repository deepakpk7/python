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

# s=input("Enter a string : ")
# r=''
# for i in s:
#     r=i+r 
# print("Reverse a String :",r)

# for i in range(4):
#     print("i=",i)
#     for j in range(3):
#         print("\tj=",j)

# for i in range(5):
#     for j in range(5):
#         print(j,end="\t")
#     print()

# for i in range(5):
#     a=1
#     for j in range(23):
#         print(a,end="\t")
#         a+=1
#     print("*")
    
# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#     print()

""" 0 0 0
    1 1 1
    2 2 2"""

# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#         i+=1
#     print()

"""
    0 1 2
    1 2 3
    2 3 4
"""
# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=1
#     print()
    

"""
    0 1 2
    3 4 5
    6 7 8 """


# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end="\t")
#     else:
#         for j in range(3):
#             print(2-j,end="\t")
#     print()
# """
""" 0   1   2
    2   1   0
    0   1   2
    2   1   0"""

# for i in range(4):
#     if(i%2==0):
#         for j in range(3):
#             print(j,end="\t")
#     print()

"""
    0   1   4
    0   1   4
    9   16  25
    9   16  25"""


# for i in range(3):
#     for j in range(3):
#         if j==0:
#             print('A',end="\t")
#         elif j==1:
#             print('B',end="\t")
#         elif j==2:
#             print('C',end="\t")
#     print()

for i in range(3):
    a=65
    for j in range(3):
        print(chr(a+j),end=" ")
    print()
"""
65 66 67
65 66 67
65 66 67
"""

"""
A B C
A B C 
A B C"""

# a=1
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=2
#     print()

# 1       3       5
# 7       9       11
# 13      15      17


