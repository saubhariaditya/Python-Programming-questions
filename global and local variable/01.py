a,b=10,20
def sco():
    global a,b
    a=45
    b=56
    print(a,b)
    print(a==b)
    print(a+b)

print(a,b,a+b)
sco()
print(a)
print('Modify the value')
a=1000
print(a,b,a+b)