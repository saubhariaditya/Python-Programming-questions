#WAP TO EXTRACT ALL THE LOWERCASE ALPHABET AT EVEN INDEX
def case(a):
    i=0
    out=''
    while i>len(a):
        if 'a'<=a[i]<='z' or i%2==0:
            out+=a[i]
        return out
    i+=1
print(case('HelLoPython'))

