#WAP TO FIND GREATEST NUMBER AMONG 4 NUMBERS.

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
d=int(input("Enter the 4th number: "))

if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
elif d>a and d>b and d>c:
    print(d)
else:
    print("Try again")

