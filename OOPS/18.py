class a:
    a=10
    b='hello'
class b(a):
    c='20'
    d='python'
class c(b):
    e='30'
    f='world'

print(c.b,c.d,c.f)
