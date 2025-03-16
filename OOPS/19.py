##  Resume  ##
class me:
    name='Aditya'
    age='23'
    school='KV IFFCO'
    number=8700728516
class Tenth(me):
    cname="Tenth"
    t_passing ='2017'
    t_percentage='83%'
    t_board='CBSE'
class diploma(Tenth):
    d_name='Diploma in mechanical production'
    d_passing ='2020'
    d_percentage='78%'
    d_board='UPBTE'
class btech(diploma):
    b_bname='Btech In Information Technology'
    b_='70%'
    b_board='AKTU'

class resume(btech):
    print(":::::::::::::RESUME:::::::::::::")
print(me.name,me.age,me.school,me.number)
print(resume.cname,resume.t_passing,resume.t_board)
print(resume.d_name,resume.t_percentage,resume.t_board)
print(resume.b_bname,resume.b_,resume.b_board)




class tenth:
    def __init__(self,name,std,rollno,percentage):
        self.name=name
        self.std=std
        self.rollno=rollno
        self.percentage=percentage
class diploma(tenth):
    def __init__(self,name,std,rollno,percentage,d_percantage,passout,college):
        super().__init__(name,std,rollno,percentage)
        self.d_percantage=d_percantage
        self.passout=passout
        self.college=college
class btech(diploma):
    def __init__(self,name,std,rollno,percentage,d_percantage,passout,college,b_percentage,b_passout,b_college)
        super().__init__(name,std,rollno,percentage,d_percantage,passout,college)
        self.b_percentage=b_percentage
        self.b_passout=b_passout
        self.b_college=b_college

Aditya=me('Aditya','X',4234123,72.2, 78, 2020, 'IIMT', 76, 2024, 'NIET')
