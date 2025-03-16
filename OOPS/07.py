#WAP TO CREATE CLASS COMPANY WITH FOUR CLASS MEMBERS, 2 OBJECTS WITH MIN 6 OBJECT MEMBERS:

class company:
    cname='google'
    cloc='uganda'
    cCEo='abhisekh'

    def __init__(self,name,age,phno,email,quali,addr):
        self.name=name
        self.phno=phno
        self.email=email
        self.quali=quali
        self.addr=addr

    def disp_obj(self):
        print(self.name,self.phno,self.email,self.quali,self.addr)

    def ch_phno(self, new):
        self.new=new

ritik=company('ritik',23,35436646364,'ritik@gmail.com','B.tech','Vanarasi')
ujjwal=company('ujjwal',21,34364773,'ujjwal@gmail.com','BCA','UP')

ritik.disp_obj()
company.disp_obj(ujjwal)
ujjwal.ch_phno(1234567888)
ujjwal.disp_obj()