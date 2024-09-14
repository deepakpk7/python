print("**********INSTAMART MANAGEMENT SYSTEM**********")

employees = []
products = []

while True:
    print("""
    1. Add Employee
    2. Display Employee Details
    3. Add Product
    4. Display Product Details
    5. Employee Management (Update)
    6. Product Management (Update)
    7. Exit
    """)
    
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Name: ")
        emp_mob = int(input("Enter Mobile Number: "))
        emp_position = input("Enter Position: ")
        emp_salary = float(input("Enter Salary: "))
        employees.append({'emp_id': emp_id,'name': emp_name,'mob': emp_mob,'position': emp_position,'salary': emp_salary})
        print("Employee added successfully!")
        
    elif choice == 2:
        if not employees:
            print("No employees to display.")
        else:
            print('_' * 70)
            print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('Emp_ID', 'Name', 'Mobile', 'Position', 'Salary'))
            print('*' * 70)
            for emp in employees:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(emp['emp_id'], emp['name'], emp['mob'], emp['position'], emp['salary']))

    elif choice == 3:
        name = input("Enter Product Name: ")
        bar_code = int(input("Enter Bar Code: "))
        price = float(input("Enter Price: "))
        products.append({'name': name, 'code': bar_code, 'price': price})
        print("Product added successfully!")

    elif choice == 4:
        if not products:
            print("No products to display.")
        else:
            print('_' * 30)
            print('{:<10}{:<10}{:<10}'.format('Product', 'Bar Code', 'Price'))
            print('*' * 30)
            for i in products:
                print('{:<10}{:<10}{:<10}'.format(i['name'], i['code'], i['price']))

    elif choice == 5:
        emp_id = int(input("Enter Employee ID to Update: "))
        for i in employees:
            if i['emp_id'] == emp_id:
                print("Current Details: ", i)
                i['name'] = input("Enter New Name: ") 
                i['mob'] = int(input("Enter New Mobile Number: "))
                i['position'] = input("Enter New Position: ")
                i['salary'] = float(input("Enter New Salary: "))
                print("Employee details updated successfully!")
                break
        else:
            print("Employee not found!")

    elif choice == 6:
        bar_code = int(input("Enter Product Bar Code to Update: "))
        for i in products:
            if i['code'] == bar_code:
                print("Current Details: ", i)
                i['name'] = input("Enter New Product Name: ")
                i['price'] = float(input("Enter New Price: "))
                print("Product details updated successfully!")
                break
        else:
            print("Product not found!")
    elif choice == 7:
        print("Exiting the system...")
        break

    else:
        print("Invalid choice! Please try again.")
