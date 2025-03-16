#WAP TO EXTRACT ALL THE INTEGER FROM A GIVEN LIST BUT INT SHOULD BE PALINDROME


a=[101,'Hello',97,121,999,123,3.5,777]
i=0
out=[]
while i<len(a):
    if type(a[i])==int and str(a[i])==str(a[i])[::-1]:
        out+=[a[i]]
    i+=1
print(out)