def val(a):
    for i in a:
        if type(i)==int and str(i)==str(i)[::-1]:
            yield (i,len(str(i)))
print(tuple(val((12,111,'hello',3.4,7777,'python'))))
