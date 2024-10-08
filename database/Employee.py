import sqlite3

con=sqlite3.connect('python/database/emp.db')
try:
    con.execute("create table employee(emp_id,name,position,salary)")
except:
    print("Table exist")

while True:
    print(""""
          1.Add Employee
          2.View Employee
          3.Update Employee
          4.Search Employee
          5.Delete Employee
          6.Exist
        """)
    choices=int(input("Enter the choices :"))
    if choices==1:
        id=int(input("Enter employee ID :"))
        name=input("Enter Name :")
        position=input("Enter the position:")
        salary=float(input("Enter salary :"))
        con.execute('insert into employee(emp_id,name,position,salary)values(?,?,?,?)',(id,name,position,salary,))
        con.commit()
    elif choices==2:
        data=con.execute("select * from employee")
        print('_' * 60)
        print('{:<10}{:<10}{:<10}{:<10}'.format('EMP ID','NAME','POSITION','SALARY'))
        print('*' * 60)
        for i in data:
            print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    elif choices==3:
        while True:
            print("""
                  1.Update ID
                  2.Update Name
                  3.Update Position
                  4.Update Salary""")
            sub_cho=int(input("Enter chices :"))
            if sub_cho==1:
                
                
            elif sub_cho==2:
                name=input("Target name :")
                nname=input("Enter new name: ")
                con.execute("update student set name=? where name=? ",(nname,name))
                con.commit()