def greatest():
    a=[0,34,54,22,11,76,89,4467,35,7467]
    great=0
    for i in a:
        if i>great:
            great=i
    return great
print(greatest())