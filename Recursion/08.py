a=['Two','Zero','Eight']
b=['Four','Three','Nine']
def get(l):
    d={'One':'1','Two':'2','Zero':'0','Three':'3','Four':'4','Eight':'8','Nine':'9'}
    out=''
    for i in l:
        out+=d[i]
    return int(out)
print(get(b))
a=['Two','Zero','Eight']
b=['Four','Three','Nine']
print(get(a)+get(b))


#WAP TO EXTRACT ALL THE LOWERCASE ALPHABET AT EVEN INDEX


