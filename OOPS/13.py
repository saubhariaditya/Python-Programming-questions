class qspider():
    batch_code='M1'
    room_no='B2'
    loc="Noida"

    def __init__(self, name, email, phno, course, time):
        self.name=name
        self.email=email
        self.phno=phno
        self.course=course
        self.time=time


    def disp_obj(self):
        print(self.name, self.email, self.phno, self.course, self.time)

    @classmethod
    def dis_cls(cls):
        print(cls.batch_code, cls.room_no,cls.loc)

aditya=qspider('Aditya', 'saubhariaditya@gmail.com', 55476569, 'python', '10:00am')
shivam=qspider('Shivam','shivam@gmail.com',54654536,'java','3:00pm')

aditya.disp_obj()