class A:
    a=100
    b=200
class B(A):
    pass
class C(A):
    def __init__(self,p,q):
        self.p=p
        self.q=q
    p=900
    q=200
class D(A):
    e=1019

print(A.a,A.b,A.p,A.q,A.e)
        