'''
a=abacdabcdaabd
output=a5b3cd3

'''

'''a='abacdabcdaabd'
a1=a.count('a')
b=a.count('b')
c=a.count('c')
d=a.count('d')
e=print('a',a1,'b',b,'c',c,'d',d)'''

a='abacdabcdaabd'
out=''
i=0
while i<len(a):
    if a[i] not in out:
        out+=a[i]+str(a.count(a[i]))
    i+=1
print(out)


