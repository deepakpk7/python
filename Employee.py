import datetime

employee=[]
while True:
    print(
        '''
1.Register Employee
2.Display Employees
3.Update Employee Deatils
4.Delete Employee
5.Add Task
6.Search Employee
7.Exit''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        id=int(input('Enter employee ID : '))
        name=input('Enter name of the employee : ')
        age=int(input('Enter age of the employee : '))
        mobile=int(input('Enter mobile number : '))
        position=input('Enter position of the employee : ')
        salary=int(input('enter salary of the employee : '))
        position=input('Enter place of the employee : ')
        employee.append([id,name,age,position,salary,mobile,position])
    elif ch==2:
        print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format('ID','NAME','AGE','POSITION','SALARY','MOBILE','POSSITION'))
        print('-'*100)
        for i in employee:
            print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif ch==3:
        id=int(input('Enter ID of the employee that you want to update : '))
        f=0
        for i in employee:
            if id in i:
                f=1
                while True:
                    print(
                    '''
                    1.Update Age
                    2.Update salary
                    3.Update position
                    4.Update experiences
                    5.Exit''')
                    sub_cho=int(input("Enter the Employee upadte choices :"))
                    if sub_cho==1:
                        new_age=int(input("Enter a new Age :"))
                        i[2]=new_age
                    elif sub_cho==2:
                        new_salary=int(input("Enter a new salary :"))
                        i[4]=new_salary
                    elif sub_cho==3:
                        new_position=input("Enter a new position :")
                        i[3]=new_position
                    elif sub_cho==4:
                        new_experiences=int(input("enter a new"))
                        i[6]=new_experiences
                    elif sub_cho==5:
                        break
            else:
                print("Employee ID not found")
    elif ch==4:
        id=input("Enter the Employee ID :")
        f=0
        for i in employee:
            if i[0]==id:
                employee.remove(i)
                f=1
        if f==0:
            print("Name Not the Database")
    elif ch==5:
        id=input("Enter the Employee ID :")
        for i in employee:
            if i[0]==id:
                f=0
                task=input("Enter a Task :")
                date=datetime.datetime.now().strftime("%x")
                i.append([task,date])
        if f==0:
            print("Employee not found ")
    elif ch==6:
        id=int(input('Enter ID of the employee that you want to search : '))
        f=0
        for i in employee:
            if id in i:
                f=1
                print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format('ID','NAME','AGE','POSITION','SALARY','MOBILE','POSSITION'))
                print('-'*100)
                print('{:<10}{:<20}{:<5}{:<20}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif ch==7:
        break
    else :
        print("***Invalid Choise***")
