#WAP TO CREATE A BANK WITH MI 3 CLASS MEMEBRS , 2 OBJECTS WITH MIN 5 OBJECT MEMBERS AND A DEPOSITE AND WITHDRAWL FUNCTION

class bank:
    bname='ICICI'
    bloc='Delhi'
    bIFSC='ICICI5786978'

    def __init__(self,name,age,phno,addr,email,bal):
        self.name=name
        self.age=age
        self.phno=phno
        self.addr=addr
        self.email=email
        self.bal=bal

    def disp_obj(self):
        print(self.name,self.age,self.phno,self.addr,self.email,self.bal)

    def deposit(self,amt):
        self.bal=self.add(self.bal,amt)

    def withdraw(self,amt):
        if amt>self.bal:
            print("Insufficient bal ")
        else:
            self.bal=self.sub(self.bal,amt)

    @classmethod
    def disp_cls(cls):
        print(cls.bname,cls.bloc,cls.bIFSC)

    @classmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def sub(a,b):
        return a-b

ankita=bank('ankita',25,655475454,'noida sec-55','ankita@gmail.com',87000000)
abhisekh=bank('abhisekh',21,98256265775,'sector 65','abhi@gmail.com',1000000)

bank.disp_cls()
ankita.disp_obj()
abhisekh.disp_obj()
abhisekh.deposit(500000000)
abhisekh.disp_obj()
abhisekh.withdraw(1245)
