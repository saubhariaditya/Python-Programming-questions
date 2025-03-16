#WAP TO CHECK NUMBER IS EVEN OR ODD:::

def even(n):
    if n%2==0:
        return True
    return False
print(even(6))

##Lambda:::::

even=lambda num:num%2==0
print(even(62))

even=lambda num:print(num%2==0)
even(32)