# def fun():
#     print("python")
#     print("HTML")
#     print("Fullstack")
    
# fun()
# print("*"*10)
# fun()
# print("*"*10)
# fun()


# def fun1():
#     a=10 #local variable
#     print(a)
#     print(b)
# a=5
# b=20 #global variable
# print(b)
# print(a)

# fun1()

# def fun2():
#     global a
#     a=10
#     print(a)
# print("Local into Global",a)
# fun2()


# def fun3():
#     return 'welcome',10

# a,b=fun3()
# print(a)
# print(b)


# def fun4():
#     a=1
#     b=2
#     c=3
#     return a,b,c
# a1,b2,c3=fun4()
# print(a1)
# print(b2)
# print(c3)


# Types of Arguments

# Position Argument
# def details(name,age):
#     print("Name :",name)
#     print("Age :",age)
# details('Deepak',20)

# Keyword Argument
# details(age=20,name='Deepak')

#Default Argument

# def sample(name='deepak',age=21):
#     print(name,age)
# sample()
# sample('deepak')
# sample(age=25)

# Aribritary Argument

# def aa(c,b,*a):
#     print(c,b,a)
    
# aa(5,6)
# aa(3,344,553,5,4)
# aa(9,4)

# Aribritary keyword Argument 

# def aka(**a):
#     print(a)
    
# aka(name='anu',age=20,name1='anu',age1=20)


def numbers():
    a=int(input("Enter a fist no :"))
    b=int(input("Enter a second no :"))
    return a,b
add=lambda a,b:numbers()
print(add(a+b))





