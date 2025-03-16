#WAP TO EXTRACT ALL THE vowle ALPHABET FROM THE GIVEN STRING

def ext_vowle():
    a=input("Enter a string:  ")
    out=''
    for i in a:
        if i in 'AEIOUaeoiu':
            out+=i
    print(out)
ext_vowle()
