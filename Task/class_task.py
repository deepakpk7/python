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
        name = input("Enter a Name: ")
        bar_code = int(input("Enter bar_code: "))
        price = int(input("Enter price: "))
        products.append({'bar_code':bar_code,'price':price})
        print(products)
    elif choice == 2:
        print('_' * 30)
        print('{:<10}{:<5}{:<5}'.format('Name', 'bar_code', 'price'))
        print('*' * 30)
        for i in products:
            print('{:<10}{:<5}{:<5}'.format(name, i['bar_code'], i['price']))
    elif choice == 3:
        name = input("Enter a Name: ")
        if name in products:
            bar_code = int(input("Enter a new bar_code: "))
            price = int(input("Enter a new price: "))
            products[name] = {'bar_code': bar_code, 'price': price}
        else:
            print("Name Not in the Database")
    elif choice == 4:
        name = input("Enter the product name to Delete: ")
        f=0
        if name in products:
            products.pop(name)
            f=1
        if f==0:
            print("product Not in the Database")
    elif choice == 5:
        name = input("Enter a Name: ")
        if name in products:
            print('{:<10}{:10}{:<10}'.format('Name','bar_code','price'))
            print('{:<10}{:10}{:<10}'.format(name, products[name]['bar_code'], products[name]['price']))
        else:
            print("***product not found***")
    
    elif choice == 6:
        break
    else:
        print("Invalid Choice")