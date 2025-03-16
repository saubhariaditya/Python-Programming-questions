a='Python is very easy'.split()

out={}
i=0
while i<len(a):
    out[a[i]]=a[i][::-1]+str(len(a[i]))
    i+=1
print(out)