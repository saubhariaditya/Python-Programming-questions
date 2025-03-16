###PRIVATE##

class Student:

    cname='python'
    cbatch='M1'
    cloc='Noida'

    def __init__(self,name,roll,mockrating):
        self.name=name
        self.roll = roll
        self.__mockrating=mockrating

    def disp_obj(self):
        print("name",self.name)
        print("roll",self.roll)

    @classmethod
    def __disp_cls(cls):
        print("cname",cls.cname)
        print("cloc",cls.cloc)

    def __displayRollAndBranch(self):

        print("name", self.name)
        print("cbatch:", self.cbatch)
        print("Mockrating:", self.__mockrating)

stu = Student("sameer", 1123444, "A+")
Student._Student__disp_cls()
#print(Student._Student__branch)
stu._Student__displayRollAndBranch()

    