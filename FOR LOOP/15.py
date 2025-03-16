# a=[10,3+5j,'Hello',321]
#op=[1,6]
a=[10,3+5j,'Hello',321]
out=[]
for i in a:
    sum=0
    if type(i)==int:
        for i in str(i):
           sum+=int(i)
        out+=[sum]
print(out)
