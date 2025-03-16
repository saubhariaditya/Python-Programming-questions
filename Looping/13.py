a='DaTAScienCE'
out=''
i=0
c=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        out+=a[i]
        c+=1
    i+=1
print(out,c)

print(out+str(c))