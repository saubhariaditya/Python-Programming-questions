class bank:
    bname='PNB'
    bloc='delhi'
    bIFSC='PNB883674'

    def __init__(self,name,age,addr,email,phno):
        self.name=name
        self.age=age
        self.addr=addr
        self.email=email
        self.phno=phno

ob1=bank('kirti',22,'delhi','kirti@gmail.com',273663873)
# ob2=bank()

# bank.data(ob1,'kirti',22,'delhi','kirti@gmail.com',273663873)
# bank.data(ob2,'kirti sharma',21,'noida','ki@gmail.com',4432167896)

print(ob1.bname,ob1.bloc,ob1.bIFSC)
print(ob1.name,ob1.addr,ob1.age,ob1.phno,ob1.email)