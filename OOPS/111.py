class Noida:
    sector=22
    block='d'

    def __init__(self,name,address,phno):
        self.name=name
        self.address=address
        self.phno=phno
    
    def disp_obj(self):
        print(self.name,self.address,self.phno)


Aditya=Noida('Aditya','d-82',75875972)

Aditya.disp_cls()
