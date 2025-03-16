a='Hello'
b='bye'

# output= 'Hbeylelo'
i=0
out=''
while i<len(a) or i<len(b):
    if i<len(a):
        out+=a[i]
    if i<len(b):
        out+=b[i]
    i+=1
print(out)   