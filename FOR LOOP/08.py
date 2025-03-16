a='abrstqz'
out=''

for i in a:
    if 'a'<=i<='y':
        out+=chr((ord(i)+1))
    else:
        out+='a'
print(out)