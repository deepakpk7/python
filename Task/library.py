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


while True:
    print("""
          1.Register
          2.Login
          3.Exist""")
    choice=int(input("Enter ur choices :"))
    if choice==1:
        register()
    elif choice==2:
        