from abc import ABC,abstractmethod
class Syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print("python")
    def php(self):
        print("php")
class Staff(Syn):
    def reg(self):
        print('staff Detalis')
    def notes(self):
        print("Notes")
class std(Syn):
    def reg(self):
        print('Student Data')
    def exam(self):
        print("Exams")
        
Staff1=Staff()
Staff1.reg()

d=std()
d.exam()