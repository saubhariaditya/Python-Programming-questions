#WAP 
# A='how are you all fellows'
# op=[1,2,2,1,2]

a ='how are you all fellows'
out=[]
for i in a:
    c=0
    for j in i:
        if j in 'AEIOUaeiou':
            c+=1
    out+=[c]
print(out)




