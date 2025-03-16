#a=''
#op={'P'['Python','programming'],'i':['is'],'l':['language'],}


def letter():
    a='Python is programming language'.split()
    out={}
    for i in a:
        if i[0] not in out:
            out[i[0]]=[i]
        else:
            out[i[0]]+=[i]
    return out
print(letter())




