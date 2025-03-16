#TAKE A LIST BUT IT SHOULD ACT LIKE SET

a=['Hai',10,3,'Hai',10,71,3.5,3]
i=0
out=[]
while i<len(a):
    if a[i] not in out:
        out+=[a[i]]
    i+=1
print(out)