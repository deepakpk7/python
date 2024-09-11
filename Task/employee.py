emp=[]

def login():
    usrname=input("Enter your Username :")
    passwd=input("Enter your Password :")
    f=0
    if usrname=='deepak' and passwd=='7034':
        f=1
        print("Login successfully.......")
    return f
    

def add_emp():
    id=int(input("Enter Employee ID :"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print("************ID already exist*************")

    if f1==0:
        name=input("Enter Employee Name :")
        age=int(input("Enter Employee Age :"))
        salary=float(input("EnterEmployee Salary :"))
        place=input("Enter Place :")
        dob=input("Enter Date Of Birth :")
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob})
        print("\t Employee Adding succesfully.....")

def emp_update():
        id=int(input("Enter Employee ID :"))
        f1=0
        for i in emp:
            if i['id']==id:
                f1=1
                name=input("Enter Employee Name :")
                age=int(input("Enter Employee Age :"))
                salary=float(input("EnterEmployee Salary :"))
                place=input("Enter Place :")
                dob=input("Enter Date Of Birth :")
                i['name']=name
                i['age']=age
                i['salary']=salary
                i['place']=place
                i['dob']=dob
                print("\t Employee Updating succesfully.....")
        if f1==0:
            print("***Invalid ID***")

def delete_emp():
    id=int(input("Enter Employee ID :"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
    if f1==0:
        print("Invalid ID ")

def display_emp():
    print("\t\t---EMPLOYEE DETALIS---")
    print('_' * 60)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name', 'Age', 'Salary', 'Place', 'DOB'))
    print('*' * 60)
    for i in emp:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['name'], i['age'],i['salary'],i['place'],i['dob']))
while True:
    print("""
          1.Login
          2.Exit
          """)
    choices=int(input("Enter your Choices :"))
    if choices==1:
        f=login()
        if f==1:
            while True:
                print("""
                      1.Add Employee
                      2.Update Employee
                      3.Delete Employee 
                      4.Display Employee Ditalis
                      5.Logout
                      """)

                sub_choices=int(input("Enter a choices :"))
                if sub_choices==1:
                    add_emp()
                    
                elif sub_choices==2:
                    emp_update()
                    
                elif sub_choices==3:
                    delete_emp()
                    
                elif sub_choices==4:
                    display_emp()
                    
                elif sub_choices==5:
                    print("Exiting ......")
                    break
        elif f==0:
            print("# Invalid Username and Password #")
    elif choices==2:
        print("Existing....")
        break