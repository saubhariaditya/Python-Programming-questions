#WAP TO PRINT to check the middle character or string is uppercase

ch=input("enter a string: ")
l=len(ch)
mid=l//2
if 'A'<=ch[mid]<='Z':
    print(ch[mid],"Yes it is uppercase")
else:
    print("not")

############################################################################
ch=input("Enter a string: ")
if len(ch)%2 !=0:
    m=len(ch)//2
    if 'A'<=ch[mid]<='Z':
        print(ch[m],'capital')
    else:
        print("not capital")
else:
    print("not a alphabet")