#WAP TO EXTRACT ALL THE INTEGER FROM THE GIVEN LIST USING FOR LOOP

a=[1,2,4.5,6,'Hello','Hii',90,80,70,5+8j]

out=0
for i in a:
    if type(i)==int:
        out+=i
print(out)