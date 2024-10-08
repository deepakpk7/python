import sqlite3

con=sqlite3.connect('python/database/demo.db')

try:
    con.execute("create table student(roll_no int,name text,age int,mark real)")
except:
    print("Table exist")
    
# con.execute("insert into student(roll_no,name,age,mark)values(1,'Deepak',20,80),(2,'ibin',21,68),(3,'alen',21,78),(4,'sreehari',21,87),(5,'alma',21,98)")
# con.commit()

# roll=int(input("Enter roll no :"))
# name=input("Enter Name :")
# age=int(input("Enter the age :"))
# mark=float(input("Enter mark :"))

# con.execute('insert into student(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
# con.commit()


# n=int(input("enter the limie :"))
# print("*"*20)
# for i in range(n):
#     roll=int(input("Enter roll no :"))
#     name=input("Enter Name :")
#     age=int(input("Enter the age :"))
#     mark=float(input("Enter mark :"))
#     con.execute('insert into student(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#     con.commit()

# SELECT * FROM

# data=con.execute("select * from student")
# # print(data)
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MARK'))
# print('*' * 60)
# for i in data:
#     # print(i[0])
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    
    
# USING CONDITION

# data=con.execute("select * from student where roll_no=2")
# # print(data)
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MARK'))
# print('*' * 60)
# for i in data:
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    
    


# print(data)
# n=int(input("Enter the value :"))
# data=con.execute("select * from student where roll_no=?",(n,))

# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MARK'))
# print('*' * 60)
# for i in data:
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))

# USING IF 
# for i in data:
#     if n==i[0]:
#         print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))

# UPDATING 


# name=input("Target name :")
# nname=input("Enter new name: ")
# con.execute("update student set name=? where name=? ",(nname,name))
# con.commit()

r=input("Enter the deiete student Roll no :")
con.execute("delete from student where roll_no=? ",(r,))
con.commit()

    
    



    