#WAP TO EXTRACT ALL THE INTEGERS FROM A GIVEN LIST::::

def ex_int(a):
    for i in a:
        if type(i)==int:
            yield i
print(list(ex_int([12,4,3,98,'hello',[2,3],76])))