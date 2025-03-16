#WAP TO EXTRACT ALL THE UPPERCASE ALPHABET FROM THE GIVEN STRING USING WHILE LOOP::::::::::::

def cap(a,i=0,out=''):
    if i>len(a):
          return out
    if 'A'<=a[i]<='Z':
            out+=a[i]
    return(a,i+1,out)
print(cap('hellLLo HhHooo'))
    

