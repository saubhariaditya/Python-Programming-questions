#WAP TO EXTRACT ALL THE INTEGER FROM THE GIVE LIST

a=eval(input("enter the list: "))
out=[]
i=0
while i<len(a):
    if type(a[i])==int:
        out+=[a[i]]
    i+=1
print(out)