students = {}

while True:
    print("""
    1. Add Student 
    2. Display Student Details
    3. Update Student
    4. Delete Student
    5. Search a Student
    6. Exit
    """)
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        name = input("Enter a Name: ")
        age = int(input("Enter Age: "))
        mark = int(input("Enter Mark: "))
        students[name] = {'age': age, 'mark': mark}
    elif choice == 2:
        print('_' * 30)
        print('{:<10}{:<5}{:<5}'.format('Name', 'Age', 'Mark'))
        print('*' * 30)
        for name, d in students.items():
            print('{:<10}{:<5}{:<5}'.format(name, d['age'], d['mark']))
    elif choice == 3:
        name = input("Enter a Name: ")
        if name in students:
            age = int(input("Enter a new Age: "))
            mark = int(input("Enter a new Mark: "))
            students[name] = {'age': age, 'mark': mark}
        else:
            print("Name Not in the Database")
    elif choice == 4:
        name = input("Enter the Name to Delete: ")
        f=0
        for i in students:
            if students[i] ==name:
                students.pop('name')
                f=1
        if f==0:
            print("Name Not in the Database")
    elif choice == 5:
        name = input("Enter a Name: ")
        if name in students:
            print('{:<10}{:<5}{:<5}'.format('Name', 'Age', 'Mark'))
            print('{:<10}{:<5}{:<5}'.format(name, students[name]['age'], students[name]['mark']))
        else:
            print("***Student not found***")
    
    elif choice == 6:
        break
    else:
        print("Invalid Choice")