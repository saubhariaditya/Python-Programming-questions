#WAP TO EXTRACT ALL THE UPPERCASE ALPHABET FROM THE GIVEN STRING


a=input("Enter the String: ")
out=' '
i=0
while i<len(a):
    if 'A'<a[i]<='Z':
        out+=a[i]
    i+=1
print(out)