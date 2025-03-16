#WAP TO EXTRACT ALL THE INTEGERS FROM THE GIVEN LIST

a=[1,'Hello','hai',4,3+5j,5]
i=0
out=[]
while i<len(a):
    if type(a[i])==int:
        out+=[a[i]]
    i+=1
print(out)


def recu(a,i=0,out=[]):
    if i>=len(a):
        return out
    if type(a[i])==int:
        out+=[a[i]]
    return recu(a,i+1,out)
print(recu([1,'Hello','hai',4,3+5j,5]))

