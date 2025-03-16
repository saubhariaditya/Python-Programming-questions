#WAP TO EXTRACT ALL THE UPPERCASE ALPHABET FROM A STRING AT EVEN INDEX:

a=input("Enter the String: ")
out=' '
i=0
while i<len(a[i]):
    if 'A'<a[i]<='Z':
        out+=a[i]
    i+=2
print(out)