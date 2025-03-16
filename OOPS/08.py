#WAP to create class hospital with 4 class members, 2 patient and 2 changes in object property

class hospital:
    hname='GIMS'
    hloc='Noida'
    hemail='gims@gail.com'
    hphno='0582455987'

    def __init__(self,name,age,disease,bloodgroup,gender,addr,phno):
        self.name=name
        self.age=age
        self.disease=disease
        self.bloodgroup=bloodgroup
        self.gender=gender
        self.addr=addr
        self.phno=phno

    def disp_patient(self):
        print(self.name,self.age,self.disease,self.bloodgroup,self.gender,self.addr,self.phno)
    
    def ch_bloodgroup(self, newbloodgroup):
        self.bloodgroup=newbloodgroup

Amrit=hospital('Amrit', '45' ,'Dengue', 'A+', 'Male', 'Noida', '76274698')
Sumit=hospital('Sumit', '32','Sinus','B-','Male','Delhi','225467654')


        