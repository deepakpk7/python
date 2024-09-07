php=set()
limit=int(input("Enter a limit php:"))
for i in range(limit):
    name=input("Enter a Names :")
    php.add(name)
print(php)
python=set()
limit1=int(input("Enter a limit python :"))
for i in range(limit1):
    name=input("Enter a Names :")
    python.add(name)
print(python)
java=set()
limit1=int(input("Enter a limit java :"))
for i in range(limit1):
    name=input("Enter a Names :")
    java.add(name)
print(java)

# a=php.intersection(python)
# a.intersection(java)
# print("Common Name:",a)
b=python.difference(php)
b.difference(java)
print("Python differend",b)

