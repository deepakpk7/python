lms=[{'id':102,'name':'deepak','place':'kozhikode','address':'TDY','mobile_no':7034622523,'email_id':'deepakpk@gmail.com','password':'7034','books':[]}]
books=[{'b_id':11,'book_name':'death note','stock':5,'price':10},{'b_id':12,'book_name':'black clover','stock':7,'price':500}]

def register():
    if len(lms)==0:
        id=101
    else:
        id=lms[-1]['id']+1
    email=input('enter your email id: ')
    f=0
    for i in lms:
        if i['email_id']==email:
            f=1
            print('already existing!!!')
            register()
    if f==0:
        name=input('enter your name: ')
        place=input('enter your place: ')
        address=input('enter your address: ')
        mob=int(input('eneter your mobile number: '))
        password=input('set your password: ')
        lms.append({'id':id,'name':name,'place':place,'address':address,'mobile_no':mob,'email_id':email,'password':password,'books':[]})
        print('registration successfull')
def login():
    uname=input("Enter your username (email id) :")
    password=input("Enter your password :")
    f=0
    if uname=='admin' and password=='admin':
        f=1
    user=''
    for i in lms:
        if uname==i['email_id'] and password==i['password'] :
            f=2
            user=i
    return f,user
def add():
    if len(books)==0:
        id=10
    else:
        id=books[-1]['b_id']+1
    bname=input("Enter the name of book :")
    stock=int(input("Enter the stock :"))
    price=float("Enter book prices :")
    books.append({'b_id':id,'book_name':bname,'stock':stock,'price':price})
def view_books():
    print('_'*40)
    print("{:<10}{:<15}{:<10}{:<10}".format('book_id','book_name','stock','price'))
    print('_'*40)
    for i in books:
        print("{:10}{:15}{:10}{:10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))
def book_update():
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
def delete_book():
    id=int(input("Enter book id you want to delete :"))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            books.remove(i)
            print("Book Delected successfully.......")
        if f==0:
            print("Invalid id!!!!!!!")

def view_users():
    print("*"*80)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mobile_no','email id'))
    print("_"*80)
    for i in lms:
        print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['place'],i['address'],i['mobile_no'],i['email_id']))

def view_profile(user):
    print('_'*85)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mobile_no','email id'))
    print('-'*85)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(user['id'],user['name'],user['place'],user['address'],user['mobile_no'],user['email_id']))

def take_book():
    id=int(input("Enter book id you want take :"))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            if i['stock']>0:
                user['books'].append(i['b_id'])
                i['stock']-=1
            else:
                print("The Book is Out off stock...")
    if f==0:
        print("Invalid id /////")
def return_book():
    id=int(input('enter the book id: '))
    f=0
    for i in books:
        if i['b_id']==id and id in user['books']:
            f=1
            user['books'].remove(id)
            i['stock']+=1
        if f==0:
            print("Book Not Found in Stock..")

def book_hand(user):
    print(user['books'])


while True:
    print("""
          1.Register
          2.Login
          3.Exist""")
    choice=int(input("Enter ur choices :"))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print("""
                      1.Add Books
                      2.View Books
                      3.Update Books
                      4.Delete Books
                      5.View Users
                      6.Logout
                      """)
                sub_choice=int(input("Enter above choices :"))
                if sub_choice==1:
                    add()
                elif sub_choice==2:
                    view_books()
                elif sub_choice==3:
                    book_update()
                elif sub_choice==4:
                    delete_book()
                elif sub_choice==5:
                    view_users()
                elif sub_choice==6:
                    print("Logouting*******************")
                    break
                else:
                    print("Enter correct Choices..")
        elif f==2:
            while True:
                print("""
                      1.View Profile
                      2.View Books
                      3.Take a Book
                      4.Return Book
                      5.Book in Users
                      6.Logout
                      """)
                user_choice=int(input("Enter Choices :"))
                if user_choice==1:
                    view_profile()
                elif user_choice==2:
                    view_books()
                elif user_choice==3:
                    take_book()
                elif user_choice==4:
                    return_book()
                elif user_choice==5:
                    book_hand(user)
                elif user_choice==6:
                    print("Logouting.....")
                    break
                else:
                    print('invalid option!!!')
        else:
            print("Invalid Username Or Password???")
    elif choice==3:
        print("Existing......")
    else:
        print("Enter invalid option  ")
