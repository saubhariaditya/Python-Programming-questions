a='11100010011001'
b='10001100100100'
i=0
out=0
outa=0
outb=0

a_lena=int(a.count('1'))
b_lenb=int(b.count('1'))
out=(a_lena-b_lenb)
print(out)

i=0
j=0
while i<len(a):
    if a[i]=='1':
        outa+=1
    i+=1
while j<len(b):
    if b[j]=='1':
        outb+=1
    j+=1
output=outa-outb
print(output)


def dif(a,b,i=0,out=0,c=0,c1=0):
    if i>=len(a) or i>=len(b):
        return out
    if a[i]=='1':
        c+=1
    if b[i]=='1':
        c1+=1
    out=c-c1
    return dif(a,b,i+1,out,c,c1)
print(dif('11100010011001','10001100100100'))

