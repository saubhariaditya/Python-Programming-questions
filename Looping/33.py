a='Hai Hello'.split()
print(a)

#op={'Hai':['Hai',6,'iaH3'],'Hello':['Hello',10,'olleH5']}

i=0
out={}
while i<len(a):
    out[a[i]]=[a[i],len(a[i])*2,a[i][::-1]+str(len(a[i]))]
    i+=1
print(out)