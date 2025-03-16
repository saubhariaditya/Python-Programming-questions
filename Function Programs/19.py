def lst(a):
    a="Python is very easy".split()
    out={}
    for i in range (len(a)):
            if i%2==0:
                 out[a[i]]=a[i][::-1]+str(len(a[i]))
            else:
                  out[a[i]]=a[i][::-1]
    return out
print(lst("Python is very easy"))



