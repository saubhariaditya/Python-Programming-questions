#Write a program to check the collection is homo or hetrogeneous 

a=eval(input("Enter the collection "))
b=type (a[0])
print(b)
c=type (a[1])
if b==c:
    print("It is homogeneous")
else:
    print("Hetrogeneous")