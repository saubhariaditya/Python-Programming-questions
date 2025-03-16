#Write a program to check last value of list is string and it's length should be more then 4

a=list(input("Enter the list: "))
#print(type(a))

b=a[-1]

if type(b)==str and len(b)>4:
    print("Accepted")
else:
    print("Not accepted")