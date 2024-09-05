# n=int(input("Enter a Number :"))
# numbers={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
# s=''
# while n>0:
#     d=n%10
#     s=numbers[d]+' '+s
#     n//=10
# print(s)

# NESTED LIST 
l=[{'name':'a','age':20,'lang':['mal','eng']}]
print(l)
s=input("Enter new language :")
l[0]['lang'].append(s)
print(l)