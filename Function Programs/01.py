#WAP TO EXTRACT ALL THE UPPERCASE ALPHABET FROM THE GIVEN STRING

def ext_up():
    a=input("Enter a string:  ")
    out=''
    for i in a:
        if 'A'<=i<='Z':
            out+=i
    print(out)
ext_up()
