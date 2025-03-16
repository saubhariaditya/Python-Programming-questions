
a='abaecdababc'    #output={'a':4,'b':3,'c':2,'d':1,'e':1} dict

a1=a.count("a")
b1=a.count("b")
c1=a.count("c")
d1=a.count("d")
e1=a.count("e")
dict={'a':a1,'b':b1,'c':c1,'d':d1,'e':e1}
print(dict)


#Second method::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
i=0
out={}
while i<len(a):
    out[a[i]]=a.count(a[i])
    i+=1
print(out)