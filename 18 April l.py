class School:
    def __init__(self,sinf,ism,guruh):
        self.sinf=sinf
        self.ism=ism
        self.guruh=guruh

    def qwerty(self):
        return f"Siz {self.sinf}-sinfda o'qiysiz, ismiz {self.ism} va guruhingiz {self.guruh}"

class Student(School):
    def get_info(self):
        return f"Salom {self.ism} siz {self.sinf}-sinfda o'qiysiz, guruhingiz {self.guruh} "
a=School(6,"Akbar","D")
print(a.qwerty())
b=School(9,"Jaloliddin","A")
print(b.qwerty())
c=School(11,"Asqar","B")
print(c.qwerty())

j=Student(2345,"Dilshod","Q")
print(j.get_info())
