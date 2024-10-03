# class bank:
#     def __init__(self):
#         print("add bank dtls")
# class user(bank):
#     def __init__(self):
#         print("add user details")
        
# sbi=bank()

# dpk=user()

# class school:
#     def notes(self):
#         print("Hi")
# class student(school):
#     def notes(self):
#         print("heloo")
# s=student()
# s.notes()

# class school:
#     def notes(self):
#         print("NOTES")
# class stud(school):
#     def notes(self):
#         print('notes in student')
#         super().notes()

# dpk=stud()
# s=school()
# s.notes()
# dpk.notes()

class school:
    def notes(self,*sub):
        print("NOTES",sub)
class stud(school):
    def notes(self,sub):
        print('notes in student')
        super().notes('python','web',sub)
        
        
dpk=stud()
dpk.notes('hi')
