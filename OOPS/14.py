###PRIVATE##

class Student:

    cname='python'
    cbatch='M1'
    __branch='CSE and all....'

    def __init__(self,name,roll,branch):
        self.name=name
        self.__roll = roll
        self.__branch= branch

    def disp_obj(self):
        print("name",self.name)
        print("roll",self.__roll)

    @classmethod
    def __disp_cls(cls):
        print("name",cls.cname)
        print("roll",cls.cbatch)

    def __displayRollAndBranch(self):

        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

stu = Student("sameer", 1123444, "Computer Science")
#Student._Student__disp_cls()
#print(Student._Student__branch)
stu._Student__displayRollAndBranch()

    