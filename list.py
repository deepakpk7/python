# l=[10,11,'anu',5.0]
# for i in l:
#     print(i)

# """
# 10
# 11
# anu
# 5.0
# """


# l=[10,11,'anu',5.0]
# if 11 in l:
#     print("YES")
# else:
#     print("NO")

# """
# YES
# """

# l=[10,11,'anu',5.0]
# print(l[2])
# l[2]="Deepak"
# print(l)

# """
# anu
# [10, 11, 'Deepak', 5.0]
# """

# ADD
# l=[10,11,'anu',5.0]
# l.append('append')
# print(l)
# l.extend(['a','b','c'])
# print(l)
# l.insert(0,"insert")
# print(l)

# """
# [10, 11, 'anu', 5.0, 'add']
# [10, 11, 'anu', 5.0, 'add', 'a', 'b', 'c']
# ['insert', 10, 11, 'anu', 5.0, 'add', 'a', 'b', 'c']
# """

# l=[10,11,'anu',5.0]
# l.pop()
# print(l)
# """
# [10, 11, 'anu']
# """
# l.pop(2)
# print(l)
# """
# [10, 11]
# """
# l.remove(10)
# print(l)
# """
# [11]
# """
# l.clear()
# print(l)

# l=[4,2,9,8,3,11,32]
# l.sort()
# print(l)
# l.reverse()
# print(l)
# """
# [2, 3, 4, 8, 9, 11, 32]
# [32, 11, 9, 8, 4, 3, 2]
# """
# l1=l.copy()
# l1.pop(4)
# print(l)
# print(l1)

# print(l.index(2))
# """
# 1
# """


# TASK

# l=[1,5,8,10,11]
# s=0
# for i in l:
#     if i%2==0:
#         print(i)
#         s+=i
# print("SUM =",s)

# l=['welcome','hello','python']
# for i in l:
#     print(i[::-1])

# """
# emoclew
# olleh
# nohtyp
# """

# l=[1,10,5.8,'abc',2]
# s=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         s+=i
# print(s)

# """
# 18.8
# """

# l=[5,8,5,1,2,3,8,5]
# du=[]
# for i in l:
#     if i not in du:
#         du.append(i)
# print(du)
    
# """
# [5, 8, 1, 2, 3]
# """

# names=[]
# limit=int(input("Enter a limit :"))
# for i in range(limit):
#     name=input("Enter a Names :")
#     names.append(name)
# print(names)

"""
Enter a limit :3
Enter a Names :deepak
Enter a Names :ibin
Enter a Names :alen
['deepak', 'ibin', 'alen']
"""
stu=[]
limit=int(input("Enter a limit :"))
for i in range(limit):
    name=input("Enter a Names :")
    age=int(input("Enter a Age :"))
    mark=int(input("Enter a mark :"))
    stu.append([name,age,mark])
print(stu)

"""
Enter a limit :2
Enter a Names :deepak
Enter a Age :21
Enter a mark :100
Enter a Names :abc
Enter a Age :12
Enter a mark :15
[['deepak', 21, 100], ['abc', 12, 15]]
"""