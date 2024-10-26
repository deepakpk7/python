
books=[]

def add():
    id=int(input("Enter the Book id :"))
    bname=input("Enter the name of book :")
    stock=int(input("Enter the stock :"))
    price=float(input("Enter book prices :"))
    books.append({'b_id':id,'book_name':bname,'stock':stock,'price':price})
    
def update():
    id=int(input("Enter the book id to update :"))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            stock=int(input("Enter the new stock :"))
            price=float(input("Enter new price :"))
            i['stock']=stock
            i['price']=price
            print("Book updated successfully........")
    if f==0:
        print("Invalid id !!!!!!")

def remove():
    id=int(input("Enter book id you want to remove :"))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            books.remove(i)
            print("Book Delected successfully.......")
    if f==0:
        
        print("Invalid id!!!!!!!")   
def view():
    print('*'*40)
    print("{:<10}{:<10}{:<10}{:<10}".format('book_id','book_name','stock','price'))
    print('_'*40)
    for i in books:
        print("{:<10}{:<10}{:<10}{:<10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))
        
def search():
    id=int(input("Enter the id to Search: "))
    f=0
    for i in books:
        if i['b_id'] == id:
            print("*"*40)
            print('{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name','Stock','price'))
            print("_"*40)
            print("{:<10}{:<10}{:<10}{:<10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))
            break
        else:
            print("***Invalid ID***")        
        
        
        
while True:
    print("""
        1. Add Book
        2. Update Book
        3. Remove Book
        4. View Book
        5. Search Book
        6. Exist
        """)

    choice=int(input("Enter the choices :"))
    if choice==1:
        add()
        print("Book added Sucessfully.....")
    elif choice==2:
        update()
        print("Updated suceedfully....")
    elif choice==3:
        remove()
    elif choice==4:
        view()
    elif choice==5:
        search()
    elif choice==6:
        print("Existing...................")
        break
    else:
        print("INVALID CHOICES....")
        