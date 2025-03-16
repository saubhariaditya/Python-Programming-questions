# a= 1100$101*110
#op= 0011#010#001



def convert():
    a='1100$101*110'
    out=''
    for i in a:
            if i=='0':
                  out+='1'
            elif i=='1':
                  out+='0'
            else:
                  out+='#'
    print(out)
convert()
