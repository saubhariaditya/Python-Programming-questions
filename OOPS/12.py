#Protected

class Student:
    cname = 'python'
    cbatch = 'M1'
    _branch = 'CSE and all...'

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll= roll
        self._branch = branch
    
    def disp_obj(self):
        print("name",self.name)
        print('roll',self.roll)
        print('branch',self._branch)

    @classmethod
    def disp
stu=Student("Sameer", 1212122, 'Computer Science')

