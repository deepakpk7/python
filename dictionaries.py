d={'name':'deepak',
   'age':'20',
   'mark':'55'}
# print(d)
# print(d['name'])
# d['name']='achu' 
# print(d)
# d['place']='Ekm'
# print(d)

"""
{'name': 'deepak', 'age': '20', 'mark': '55'}
deepak
{'name': 'achu', 'age': '20', 'mark': '55'}
{'name': 'achu', 'age': '20', 'mark': '55', 'place': 'Ekm'}
"""

# for i in d:
    # print(i)
    # print(d[i])
    # print(i,":",d[i])
    
# if d['name']=='deepak':
#     print("Yes")
# else:
#     print("No")

# Methods

print(d.get('name'))
print(d.values())
print(d.keys())
print(d.items())
# d.pop('age')
# print(d)
# d.popitem()
# print(d)
d.update({'mark':'100'})
print(d)
# d.clear()
# print(d)
