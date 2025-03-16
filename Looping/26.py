#a=aaabcbcc
a='aaabcbcc'
i=0
c=1
out=''
while i<len(a)-1:
   if a[i]==a[i+1]:
      c+=1
   else:
      out+=a[i]+str(c)
      c=1
   i+=1
out+=a[-1]+str(c)
print(out)