#WAP
# op='a1b2a1c3d4e5a1b2' 

a='abacdeab'
out=''
for i in a:
    if 'a'<=i<='z':
        out+=i+str(ord(i)-96)
print(out)