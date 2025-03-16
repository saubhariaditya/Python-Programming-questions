a=['home.py','google.com','yahoo.in','gmail.com','pro.html']
#op= ['py','com','in','com','html']

out=[]
for i in a:
    a=i.split('.')
    out+=[a[1]]  #/[a[i]]
print(out)