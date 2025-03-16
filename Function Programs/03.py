# TO convert first letter to uppercase

def upp_case():
    a='python'
    out=''
    for i in range (len(a)):
        if i==0 and 'a'<=a[i]<='z':
            out+=chr(ord(a[i])-32)
        else:
            out+=a[i]
    print(out)
upp_case()


#capitialize()
b='hello'
print(b.capitalize())