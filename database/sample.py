import sqlite3

con=sqlite3.connect('python/database/demo.db')

try:
    con.execute("create table student(roll_no int,name text,age int,mark real)")
except:
    print("Table exist")
    
con.execute("insert into student(roll_no,name,age,mark)values(1,'Deepak',20,80),(2,'ibin',21,68),(3,'alen',21,78),(4,'sreehari',21,87),(5,'alma',21,98)")
con.commit()

# n=int(input("enter the limit"))
# print("*"*20)
# for i in range(n):
#     roll=int(input("enter roll no :"))
#     name=input("enter name :")
#     age=int(input("enter thr age :"))
#     mark=float(input("enter the mark :"))

#     con.execute('insert into student(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#     con.commit()

# data=con.execute("select * from student")
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MAEK'))
# print('*' * 60)
# for i in data:
#     # print(i[0])
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    

# USING CONDITION
# n=int(input("enter the  value"))

# data=con.execute("select * from student where roll_no=?",(n,))
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MAEK'))
# print('*' * 60)
# for i in data:
#     # print(i[0]) 
#       print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    

 
# updating


# name=input("enter the name :" )
# n_name=input("enter the second name : ")
# con.execute("update student set name=? where name=?",(n_name,name))
# con.commit()

r=input("enter the deletd student roll no :")
con.execute("delet from student where roll_no=?",(r,))
con.commit()