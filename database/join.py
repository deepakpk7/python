import sqlite3

con=sqlite3.connect('python/database/join.db')

try:
    con.execute("create table student(roll_no int,name text,age int)")
except:
    print("Table exist")
    
try:
    con.execute("create table mark(roll_no int,subject text,mark int)")
except:
    print("Table exist")
    
# con.execute("insert into student(roll_no,name,age)values(1,'Deepak',20),(2,'ibin',21),(3,'alen',21)")
# con.commit()
# con.execute("insert into mark(roll_no,subject,mark)values(1,'python',85),(2,'php',75),(4,'java',80),(1,'php',54)")
# con.commit()

# data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from student join mark on student.roll_no=mark.roll_no")

# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','SUBJECT','MARK'))
# print('*' * 60)
# for i in data:
    # print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4]))
    # print(i)
    
# data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from mark left join student on student.roll_no=mark.roll_no")
# for i in data:
#     print(i)

data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from student cross join mark")
for i in data:
    print(i)
