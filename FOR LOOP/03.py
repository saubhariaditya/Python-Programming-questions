#WAP to extract all the uppercase alphabate from the given string
a='NeHA is A GooD Girl'

out=''
for i in a:
    if 'A'<=i<='Z':
        out+=i
print(out)