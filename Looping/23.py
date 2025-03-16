'''
input= 'How are you all'
output= 'How_are_you_all'

'''

a='How are you all'
i=0
out=''
while i<len(a):
    if a[i]==' ':
        out+='_'
    else:
        out+=a[i]
    i+=1
print(out)
