products = []

while True:
    print("""
    1. Add product 
    2. Display product Details
    3. Update product
    4. Delete product
    5. Search a product
    6. Exit
    """)
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        name = input("Enter a product name: ")
        bar_code = int(input("Enter bar_code: "))
        price = int(input("Enter price: "))
        products.append({'name': name, 'bar_code': bar_code, 'price': price})
        print(products)
    
    elif choice == 2:
        print('_' * 30)
        print('{:<10}{:<10}{:<10}'.format('Product', 'bar_code', 'price'))
        print('*' * 30)
        for i in products:
            print('{:<10}{:<10}{:<10}'.format(i['name'], i['bar_code'], i['price']))
    
    elif choice == 3:
        name = input("Enter the product name to update: ")
        for i in products:
            if i['name'] == name:
                bar_code = int(input("Enter a new bar_code: "))
                price = int(input("Enter a new price: "))
                i['bar_code'] = bar_code
                i['price'] = price
                print("Product updated successfully.")
                break
        else:
            print("Product not found")
    
    elif choice == 4:
        name = input("Enter the product name to Delete: ")
        for i in products:
            if i['name'] == name:
                products.remove(i)
                print("Product removed successfully.")
                break
        else:
            print("Product not in the Database")
    
    elif choice == 5:
        name = input("Enter the product name to Search: ")
        for i in products:
            if i['name'] == name:
                print('{:<10}{:<10}{:<10}'.format('Name', 'bar_code', 'price'))
                print('{:<10}{:<10}{:<10}'.format(i['name'], i['bar_code'], i['price']))
                break
        else:
            print("***Product not found***")
    
    elif choice == 6:
        print("Existing .......")
        break
    
    else:
        print("Invalid Choice")

