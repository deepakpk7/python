stu=[]
while True:
    print("""
    1.Add Student 
    2.Display Student Details
    3.Update Student
    4.Delete Student
""")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        name=input("Enter a Names :")
        age=int(input("Enter a Age :"))
        mark=int(input("Enter a mark :"))
        stu.append([name,age,mark])
    elif choice==2:
        print('{:<10}{:<5}{:<5}'.format('Name','Age','Mark'))
        print('*'*20)
        for i in stu:
            print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input("Enter a Name")
        f=0
        for i in stu:
            if i[0]==name:
                mark=int(input("Enter a new mark"))
                i[2]=mark
                f=1
        if f==0:
            print("Name Not the Database")
