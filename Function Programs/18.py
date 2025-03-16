print("1(+),  2(-),  3(*),  4(/)")
a=int(input("Enter the first num:  "))
b=int(input("Enter the second num:  "))
e=int(input("Enter the operation:  "))

def add(a, b):
    if e==1:
        ans=a+b
    print(ans)
def sub(a, b):
    if e==2:
        ans=a-b
    print(ans)
def multi(a, b):
    if e==3:
        ans=(a*b)
    print(ans)
def div(a, b):
    if e==4:
        ans=a/b
    print(ans)
ans=0
add(a, b)
sub(a, b)
multi(a, b)
div(a, b)