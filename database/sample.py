import sqlite3

con=sqlite3.connect('python/database/demo.db')

try:
    con.execute("create table student(roll_no int,name text,age int,mark real)")
except:
    print("Table exist")
    
con.execute("insert into student(roll_no,name,age,mark)values(1,'Deepak',20,80),(2,'ibin',21,68),(3,'alen',21,78),(4,'sreehari',21,87),(5,'alma',21,98)")
con.commit()