# wap to find factorial to print all the perfect number present between range 1 to 1000 and store it in list

out=[]
for i in range(1,1000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j 
    if sum==i:
        out+=[i]
print(out)