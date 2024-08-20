# i=int(input("Enter starting value : "))
# l=int(input("enter ending value : "))
# while i<=l:
#     print(i)
#     i+=1

# i=1
# l=int(input("Enter limit : "))
# while i<=l:
#     print("*Deepak*")
#     i+=1

# SUM OF NUMBERS

# i=int(input("Enter starting value : "))
# e=int(input("enter ending value : "))
# sum=0
# while i<=e:
#     sum=sum+i
#     i+=1
# print("Sum = ",sum)

# EVEN NUMBER SUM PRINT

# i=int(input("Enter starting value : "))
# e=int(input("enter ending value : "))
# sum=0
# while i<=e:
#     if i%2==0:     
#         sum=sum+i
#     i+=1
# print("Sum of Even Numbers :",sum)

# MULTIPLICATION TABLE

# m=int(input("Enter a multiplication :"))
# i=1
# while i<=10:
#     print(i,"*",m,"=",i*m)
#     i+=1


# i=int(input("Enter a first no : "))
# e=int(input("Enter a last number : "))
# sum=0
# sum1=0
# sum2=0
# while i<=e:
#     sum=sum+i
#     if i%2==0:     
#         sum1=sum1+i
#     else :
#         sum2=sum2+i
#     i+=1
# print(sum)
# print(sum1)
# print(sum2)

# FACTORIAL OF A NUMBER

# a=int(input("Enter a number : "))
# i=1
# f=1
# while i<=a:
#     f*=i
#     i+=1
# print(f)

# REVERSE A NUMBER

# n=int(input("Enter a no :: "))
# r=0
# while n>0:
#     d=n%10
#     r=r*10+d
#     n//=10
# print("Reverse = ",r)

# SUM OF A DIGIT

# n=int(input("Enter a no :: "))
# s=0
# while n>0:
#     d=n%10
#     s=s+d
#     n//=10
# print("Sum of digit =",s)

# STRING

# s=input("Enter a string : ")
# l=len(s)
# i=0
# while i<l:
#     print(s[i])
#     i+=1

# STRING REVERSE

s=input("Enter a string : ")
l=len(s)
i=0
r=''
while i<l:
    r=s[i]+r 
    i+=1
print(r)
