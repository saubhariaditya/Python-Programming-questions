'''

a=['Hai',37, [1,2,3],'Python','Hello',3.5, 'P']
output={'Hai':3, 'Python':6,'Hello':5}


'''

a=['Hai',37,[1,2,3],'Python','Hello',3.5,'P']
i=0
out={}
while i<len(a):
    if type(a[i])==str and len(a[i])>1:
        out[a[i]]=len(a[i])
    i+=1
print(out)