# l=[10,11,'anu',5.0]
# for i in l:
#     print(i)

"""
10
11
anu
5.0
"""


# l=[10,11,'anu',5.0]
# if 11 in l:
#     print("YES")
# else:
#     print("NO")

"""
YES
"""

# l=[10,11,'anu',5.0]
# print(l[2])
# l[2]="Deepak"
# print(l)

"""
anu
[10, 11, 'Deepak', 5.0]
"""

l=[10,11,'anu',5.0]
l.append('append')
print(l)
l.extend(['a','b','c'])
print(l)
l.insert(0,"insert")
print(l)

"""
[10, 11, 'anu', 5.0, 'add']
[10, 11, 'anu', 5.0, 'add', 'a', 'b', 'c']
['insert', 10, 11, 'anu', 5.0, 'add', 'a', 'b', 'c']
"""

