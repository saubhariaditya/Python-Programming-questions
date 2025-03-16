#WAP TO PRINT ALL THE LOWERCASE ALPHABET TO UPPERCASE PRESENT INSIDE A STRING

def upper_case(a):
    out=''
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(upper_case('Python is A a programming Language'))

