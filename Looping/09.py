#EXTRACT SPECIAL CHARACTER FROM emailid

a=input("Enter the email id: ")
out = ' '
i=0
while i<len(a):
    if a[i] in '@_.':
        out+=a[i]
    i+=1
print(out)   