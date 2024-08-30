emp=[]
while True:
    print("""
    1.Employee Registration 
    2.Employee View
    3.Delete Employee
    4.Search a Employee
    5.Add Task
    6.Exist
""")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        emp_name=input("Enter a Names :")
        emp_id=int(input("Enter a Employee Id :"))
        age=int(input("Enter a Age:"))
        salary=int(input("Enter Salary :"))
        position=input("Enter Position :")
        experience=int(input("Enter Experiences :"))
        emp.append([emp_name,emp_id,age,salary,position,experience])
    elif choice==2:
        print('_'*50)
        print('{:<10}{:<5}{:<5}{:<10}{:<10}{:<10}'.format('Name','ID','Age','Salary','Position','Experiences'))
        print('*'*50)
        for i in emp:
            print('{:<10}{:<5}{:<5}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        emp_name=input("Enter the Name Employee name :")
        f=0
        for i in emp:
            if i[0]==emp_name:
                emp.remove(i)
                f=1
        if f==0:
            print("Name Not the Database")
    elif choice==4:
        emp_name=input("Enter search employee Name :")
        f=0
        for i in emp:
            if i[0]==emp_name:
                print('_'*50)
                print('{:<10}{:<5}{:<5}{:<10}{:<10}{:<10}'.format('Name','ID','Age','Salary','Position','Experiences'))
                print('*'*50)
                print('{:<10}{:<5}{:<5}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
                f=1
        if f==0:
            print("***Employee not found***")
    elif choice==5:
        print("Enter a task")
    elif choice==6:
        break
    else:
        print("Invalid Choice")