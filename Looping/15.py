#WAP TO EXTRACT ALL THE FLOAT VALUES USING IS INSTANCE

print(isinstance(8,float))
a=[1,3.5,'hello',5+4j,3.4]
out=[]
i=0
while i <len(a):
    if isinstance(a[i],float):
        out+=[a[i]]
    i+=1
print(out)