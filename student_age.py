std=[{'name':'a','age':25},
      {'name':'b','age':30},
      {'name':'c','age':20},
      {'name':'d','age':35},
      ]
b=[]
a=[]
for i in std:
    if i['age']>=30:
       a.append(i)
    else:
        b.append(i)

print("Above in 30")
print('{:<10}{:<5}'.format('Name', 'Age'))     
for i in a:
    print('{:<10}{:<5}'.format(i['name'],i['age']))
print("Below in 30")
print('{:<10}{:<5}'.format('Name', 'Age'))     
for i in b:
    print('{:<10}{:<5}'.format(i['name'],i['age']))
    