# ?SINGLE INHERITANCES

# class parent:
#     def land(self):
#         print("Land 12 ")
#     def balances(self):
#         print("1 cros")

# class son(parent):
#     def bike(self):
#         print("Bike")

# dpk=son()
# dpk.bike()
# dpk.balances()
# dpk.land()
# print('*'*40)
# class Synofo:
#     def python(self):
#         print("python ")
#     def php(self):
#         print("php")

# class nova(Synofo):
#     def web(self):
#         print("Web dev")
#     def dm(self):
#         print("Digital markting")
# anu=nova()
# anu.python()
# anu.php()
# anu.web()
# anu.dm()

# MULTIPLE INHERITANCES

# class Dad:
#     def shop(self):
#         print("Shop")
#     def car(self):
#         print("Cars")
# class Mom:
#     def kitchen(self):
#         print("Gerosaries")
#     def money(self):
#         print("100000")
        
# class Son(Dad,Mom):
#     def Bike(self):
#         print("Bike")

# a=Son()
# a.Bike()
# a.car()
# a.kitchen()
# a.money()
# a.shop()

# class school:
#     def time(self):
#         print("(9 am to 4 pm)")
#     def class_room(self):
#         print("jgnn")
# class Tution:
#     def time_t(self):
#         print("Only 2 hours")

# class student(school,Tution):
#     def books(self):
#         print("10")

# stud=student()
# stud.books()
# stud.class_room()
# stud.time()
# stud.time_t()

# MULTILEVEL INHERITANCES

# class CU:
#     def exam(self):
#         print("Exam Notification")
#     def result(self):
#         print("Supply")
# class College(CU):
#     def class_room(self):
#         print("Class rooms")
#     def assignment(self):
#         print("Internal ")
# class student(College):
#     def uniform(self):
#         print("kf")
    
# stu=student()
# stu.exam()
# stu.result()
# stu.class_room()
# stu.assignment()
# stu.uniform()

# HIEARCHICAL INHERITANCES

class College:
    def exam(self):
        print("Exam")
    def assignment(self):
        print("Internal ")
class chm(College):
    def notes(self):
        print("dfkj")
class bio(College):
    def uniform(self):
        print("kf")
        
s=chm()
s.assignment()
a=bio()
a.uniform()
        
    