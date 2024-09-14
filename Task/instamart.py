print("**********INSTAMART MANGEMENT SYSTEM**********")
instamart = []

while True:
    print("""
    1. Add Employee
    2. Display Employee Details
    3. Add product
    4. Display product Details
    5. Employee mangement
    6. Product mangement
    7. Exit
    """)
    
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        emp_id=int(input("Enter Employee ID : "))
        emp_name = input("Enter a Name: ")
        emp_mob = int(input("Enter mobile number: "))
        emp_position = input("Enter position: ")
        emp_salary=float(input("Enter a salary: "))
        instamart.append({'emp_id':emp_id,'name': emp_name, 'mob': emp_mob,'position':emp_position,'salary':emp_salary})
        print("Empolyee added successfully!")
        
    elif choice == 2:
        print('_' * 70)
        print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('Emp_ID', 'Name', 'Mobile', 'Position', 'Salary'))
        print('*' * 70)
        for i in instamart:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(i['emp_id'], i['name'], i['mob'], i['position'], i['salary']))
    
    elif choice== 3:
        print("ADDING A NEW PRODUCT ENTER THE DETAILES BELOW ")
        bar_code = int(input("Enter bar_code: "))
        name = input("Enter a product name: ")
        price = int(input("Enter price: "))
        instamart.append({'bar_code': bar_code,'name': name, 'price': price})
        print("Product added successfully!")
    
    elif choice== 4:
        print('_' * 30)
        print('{:<10}{:<10}{:<10}'.format('bar_code','Product','price'))
        print('*' * 30)
        for i in instamart:
            print('{:<10}{:<10}{:<10}'.format(i['bar_code'], i['name'], i['price']))
            
            
    elif choice == 5:
        emp_id = int(input("Enter Employee ID to Update: "))
        for i in instamart:
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
        for i in instamart:
            if i['bar_code'] == bar_code:
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
