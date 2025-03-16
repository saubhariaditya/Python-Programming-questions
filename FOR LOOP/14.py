#WAP TO FIND THE FACTORIAL OF A NUMBER 1 TO 11 AND STORE THE OUTPUT IN THE LIST:::::::::::

#a=int(input("Enter the number::  "))
out=[]
for i in range(1,11):
    fact=1
    for i in range(1,i+1):
        fact*=i
    out+=[fact]
print(out)



