a=[10,3,'Hai',3+5j,'Hai',10,3,3.3,'Hello']
op=[10,3,'Hai']
out=[]
for i in a:
    if i not in out:
        if a.count(i)>1:
            out+=[i]
print(out)


def dupli():
    out=[]
    for i in a:
        if i not in out:
            if a.count(i)>1:
                out+=[i]
    return out
print(dupli())
