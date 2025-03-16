#WAP TO EXTRACT STRING WITH MORE THAN 3 LETTERS FROM A LIST


a=['Hey',1,5,6,'Hello','Hii',5+6j,'Adiityaa','Adi']
print(len(a))
i=0
out=[]
while i<len(a):
    if type(a[i])==str and len(a[i])>3:
        out+=[a[i]]
    i+=1
print(out)
