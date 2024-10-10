import mysql.connector

con =mysql.connector.connect(host='localhost',user='deepak',password='703462',database='dpkdata')
con.autocommit=True
cur=con.cursor()
# cur.execute('create database dpkdata')
# cur.execute("create table student (roll int,name text,age int,mark int)")
# cur.execute("insert into student (roll,name,age,mark) values(1,'deepak',20,87)")

# roll=int(input("enter roll no :"))
# name=input("Enter name :")
# age=input("Emter the age :")
# mark=input("Enter mark :")

# cur.execute('insert into student (roll,name,age,mark) values(%s,%s,%s,%s)',(roll,name,age,mark))

# cur.execute("select * from student")
# data=cur.fetchall()
# for i in data:
#     print(i)

# UPDATE

# name=input("Target name :")
# nname=input("Enter new name: ")
# cur.execute("update student set name=%s where name=%s ",(nname,name))

# DELECTE 

# roll=int(input("Enter the delete student Roll no :"))
# cur.execute("delete from student where roll=%s ",(roll,))

# LIKE
# cur.execute("select * from student where name like 'a%'")
# data=cur.fetchall()
# for i in data:
#     print(i)

# ORDER BY
# cur.execute("select * from student order by name")
# data=cur.fetchall()
# for i in data:
#     print(i)

# DESCINTING ORDER
# cur.execute("select * from student order by name desc")
# data=cur.fetchall()
# for i in data:
#     print(i)

# GROUP BY
cur.execute("select * from student group by name ")
data=cur.fetchall()
for i in data:
    print(i)


# AGGRIGATE FUNCTION
# MAX()
cur.execute("select name,max(mark) from student group by name")
data=cur.fetchall()
for i in data:
    print(i)

# MIN()
cur.execute("select name,min(mark) from student group by name")
data=cur.fetchall()
for i in data:
    print(i)
    
# AVG()
cur.execute("select name,avg(mark) from student group by name")
data=cur.fetchall()
for i in data:
    print(i)

# COUNT()
cur.execute("select name,count(mark) from student group by name")
data=cur.fetchall()
for i in data:
    print(i)

