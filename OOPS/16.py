#MAGIC METHOD

class A:
    def __init__(self,a):
        self.a=a 
    def __add__(self,other):
        return self.a + other.a
    def __sub__(self,other):
        return self.a - other.a 
    def __mul__(self,other):
        return self.a * other.a     
    def __truediv__(self,other):
        return self.a / other.a 
    def __pow__(self,other):
        return self.a**other.a   
    def __mod__(self,other):
        return self.a % other.a
    def __floordiv__(self,other):
        return self.a//other.a

obj=A(10)
obj1=A(20)
print(obj+obj1)
print(obj-obj1)
print(obj*obj1)
print(obj/obj1)
print(obj**obj1)
print(obj%obj1)
print(obj//obj1)
