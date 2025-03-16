#WAP TO PRINT THE COUNT OF ALL THE UPPERCASE PRESENT IN THE GIVEN STRING ONLY IF THEY ARE AT  ODD INDEX AND
#THERE ASCII VALUE DIVISIBLE BY 3

def run():
    c=0
    out=''
    a=input("Enter the string: ")
    for i in range(len(a)):
        if 'A'<=a[i]<='Z' and i%2==0 and ord(a[i])%3==0:
            out+=a[i]
            c+=1
    return c,out
print(run())