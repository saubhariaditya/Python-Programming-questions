#output=[5,23,3+5j,'python',[1,2,3],34,4,(1,3)]

a=['hello',23,3+5j,'python',[1,2,3],34,'star',(1,3)]
def st_l(a):
    out=[]
    for i in range (len(a)):
        if type(a[i])==str and i%2==0:
            out+=[len(a[i])]
        else:
            out+=[a[i]]
    return out
print(st_l(['hello',23,3+5j,'python',[1,2,3],34,'star',(1,3)]))
