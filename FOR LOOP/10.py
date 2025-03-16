a=['home.py','google.com','yahoo.in','gmail.com','pro.html']

out={}
for i in a:
    a=i.split(".")
    if a[1] not in out:
        out[a[1]]=[a[0]]
    else:
        out[a[1]]+=[a[0]]
print(out)



