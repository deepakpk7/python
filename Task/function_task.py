def numbers():
    a=int(input("Enter a fist no :"))
    b=int(input("Enter a second no :"))
    return a,b
def add():
    a,b=numbers()
    print("Sum=",a+b)
def sub():
    a,b=numbers()
    print("Sub=",a-b)
def div():
    a,b=numbers()
    print("Div=",a/b)
def mul():
    a,b=numbers()
    print("Mul=",a*b)
def mod():
    a,b=numbers()
    print("Modu=",a%b)
while True:
    print("""
        1. Add 
        2. Substraction
        3. Multiplication
        4. Division
        5. Modules
        6. Exist
        """)
    choise=int(input("Enter ur chooices :"))
    if choise==1:
        add()
    elif choise==2:
        sub()
    elif choise==3:
        mul()
    elif choise==4:
        div()
    elif choise==5:
        mod()
    elif choise==6:
        break
    else :
        print("Invalid choces......")

