import sqlite3

con=sqlite3.connect('python/database/emp.db')
try:
    con.execute("create table employee(emp_id int,name text,position text,salary real)")
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
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))
        con.execute('INSERT INTO employee(emp_id, name, position, salary) VALUES (?, ?, ?, ?)', (emp_id, name, position, salary))
        con.commit()
        print("Employee added successfully.\n")
    elif choices==2:
        data = con.execute("SELECT * FROM employee")
        print('_' * 60)
        print('{:<10}{:<20}{:<15}{:<10}'.format('EMP ID', 'NAME', 'POSITION', 'SALARY'))
        print('_' * 60)
        for i in data:
            print('{:<10}{:<20}{:<15}{:<10}'.format(i[0], i[1], i[2], i[3]))
        print()
    elif choices==3:
        emp_id = int(input('Enter the employee ID to update: '))
        data = con.execute('SELECT * FROM employee WHERE emp_id = ?', (emp_id,))
        for i in data:
            if i[0]==emp_id:
                while True:
                    print('''
                        1. Update Name
                        2. Update Position
                        3. Update Salary
                        4. Exit
                    ''')
                    ch = int(input('Enter your choice: '))
                    if ch == 1:
                        new_name = input('Enter new name: ')
                        con.execute('UPDATE employee SET name = ? WHERE emp_id = ?', (new_name, emp_id))
                        con.commit()
                        print("Name updated successfully.\n")
                    elif ch == 2:
                        new_position = input("Enter new position: ")
                        con.execute('UPDATE employee SET position = ? WHERE emp_id = ?', (new_position, emp_id))
                        con.commit()
                        print("Position updated successfully.\n")
                    elif ch == 3:
                        new_salary = float(input("Enter new salary: "))
                        con.execute('UPDATE employee SET salary = ? WHERE emp_id = ?', (new_salary, emp_id))
                        con.commit()
                        print("Salary updated successfully.\n")
                    elif ch == 4:
                        break
                    else:
                        print("INVALID CHOICES ")
            else :
                print("INVALID ID")
    elif choices==4:
        emp_id = int(input('Enter the employee ID to search: '))
        data = con.execute('SELECT * FROM employee WHERE emp_id = ?', (emp_id,))
        for i in data:
            if i[0]==emp_id:
                print('_' * 60)
                print('{:<10}{:<20}{:<15}{:<10}'.format('EMP ID', 'NAME', 'POSITION', 'SALARY'))
                print('_' * 60)
                print('{:<10}{:<20}{:<15}{:<10}'.format(i[0], i[1], i[2], i[3]))
                print()
            else:
                print("Employee Not Found.....")
    elif choices==5:
        emp_id = int(input('Enter the employee ID to delete: '))
        con.execute('DELETE FROM employee WHERE emp_id = ?', (emp_id,))
        con.commit()
        print("Employee deleted successfully.\n")
    elif choices == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
