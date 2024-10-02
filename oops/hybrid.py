class Library:
    def Time(self):
        print("9 am to 4 pm")
    def Books(self):
        print("Available Books")
class Admin(Library):
    def staff(self):
        print("Staff")
    def staff_off(self):
        print("Off")
class Users(Admin):
    def Book(self):
        print("Book Name")
    def book_inhand(self):
        print("My Books")
class Staff(Admin):
    def salary(self):
        print("10k")
    def task(self):
        print("Task")
class Office(Staff):
    def account(self):
        print("Account manement")
class Clean(Staff):
    def room(self):
        print("Clean finished")
    def schedule(self):
        print("clean staff schedule")

deepak=Users()
deepak.Books()

a=Admin()
a.Time()

o=Office()
o.salary()

c=Clean()
c.schedule()

l=Office()
l.task()