
op={12:[12,1],'Hai':['Hai',3]}

def array_len(a):
    out={}
    for i in a:
        if i in [int,str,list,complex]:
            out[i]=[i,1]
        else:
            out[i]=[i,len(i)]
    print(out)
array_len([12,'Hai',[1,2,3],3+5j,3.5])