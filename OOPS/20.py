######## MULTIPLE INHERITANCE#########

class bat:
    b_color= 'brown'
    b_len= '90cm'
    b_weight='980gms'
class ball:
    shape='Sphere'
    color='white'
    weight='72gms'
class stumps:
    qnt='3'
    s_col='Red'

class cricket(bat, ball, stumps):
    pass

print(cricket.b_color, cricket.b_len,cricket.b_weight, cricket.shape, cricket.color, cricket.weight, cricket.qnt, cricket.s_col)
