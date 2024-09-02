stu={}
while True:
    print("""
    1.Add Student 
    2.Display Student Details
    3.Update Student
    4.Delete Student
    5.Search a Student
    6.Exist
""")
    choice=int(input("Enter ur Choice :"))
    if choice==1:
        name=input("Enter a Names :")
        age=int(input("Enter a Age :"))
        mark=int(input("Enter a mark :"))