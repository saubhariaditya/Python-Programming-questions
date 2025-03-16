class libr:
    lib={'Python': 10, 'Java': 20, 'SQL': 45}

    def __init__(self,name,phno,roll,quantity, bookname):
        self.name=name
        self.phno=phno
        self.roll=roll
        self.quantity=quantity
        self.bookname=bookname

    def submit(self,bookname):
        if self.bookname in libr.lib:
            libr.lib[self.bookname]=libr.lib[self.bookname]+1
        print(libr.lib)


    def withdraw(self,bookname):
        if self.bookname in libr.lib:
            libr.lib[self.bookname]=libr.lib[self.bookname]-1
        else:
            print('Book not avai..')
        print(libr.lib)
akash=libr('Aditya', 84583049835, 212412, 1, 'Python')
a=input("Enter the book name::  ")
if a not in libr.lib:
    print("This book is not avail...")
else:
    pass
akash.withdraw(a)


