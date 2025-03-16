a=[2,3.5,7,8,3+5j]
i=0
out=[]
while i<len(a):
    if type(a[i])==int and a[i]%2==0:
        out += [a[i] ** 2]
    else:
        out+=[a[i]]
    i+=1
print(out)

def square(a,i=0,out=[]):
    if i>=len(a):
        return out
    if type(a[i])==int and a[i]%2==0:
        out += [a[i] ** 2]
    else:
        out+=[a[i]]
    return square(a,i+1,out)
print(square([2,3.5,7,8,3+5j]))
    
    