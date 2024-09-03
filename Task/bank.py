print("**********Bank**********")
bank=[]
while True:
    print("""
    1.Add to customer
    2.Display Customers
    3.Update Customers
    4.Remove Customers
    5.Search a Customers
    6.Exist
""")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        ac_number=int(input("Enter A/C Number :"))
        name=input("Enter a Names :")
        mobile_no=int(input("Enter Mobile Number :"))
        aadhar=int(input("Enter your Aadhar Number :"))
        bank.append([ac_number,name,mobile_no,aadhar])
    elif choice==2:
        print('_'*50)
        print('{:<10}{:<5}{:<12}{:<15}'.format('AC NO','NAME','MOBILE NO','AADHAR NUMBER'))
        print('_'*50)
        for i in bank:
            print('{:<10}{:<5}{:<12}{:<15}'.format(i[0],i[1],i[2],i[3]))
    else:
        print("Invalid Choice")

