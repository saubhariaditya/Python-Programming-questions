'''WAP TO PRINT THE CLASS BANK WITH MINIMUM THREE CLASS MEMEBERS AND MINIMUM 2 OBJECTS
WITH MINIMUM 5 OBJECT MEMBERS'''

class bank:
    bname='SBI'
    bloc='Noida'     #static properties
    BIFSC='SBI0032637'

kunal=bank()
shivam=bank()

kunal.name='kunal'
kunal.addr='rohtak'   #object members
kunal.age='23'
kunal.email='kunal@123'
kunal.phno=9234538950


shivam.name='shivam'
shivam.addr='delhi'   #object members
shivam.age='21'
shivam.email='shivam@123'
shivam.phno=923433487


print(bank.bname, bank.bloc, bank.BIFSC)

print(kunal.addr, kunal.age, kunal.email, kunal.phno, kunal.name)
print(shivam.addr, shivam.age, shivam.email, shivam.phno, shivam.name)
