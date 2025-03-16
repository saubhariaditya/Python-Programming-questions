a=input("Enter your email: ")
b=''
c=''
d=''
e=''
i=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        b+=a[i]
    elif 'a'<=a[i]<='Z':
        c+=a[i]
    elif '1'<=a[i]<='9':
        d+=a[i]
    else:
        e+=a[i]
    i+=1
print(b, c, d, e)
            