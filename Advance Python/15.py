#WAP TO EXTRACT ALL THE FACTORIAL NUMBERS PRESENT IN BETWEEN RANGE 1 TO 1000..
#import math
#fact=lambda num:math.factorial(num)
#out=map(fact,range(1,11))
#print(list(out))


def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

out=[]
for i in range(1,10):
    if fact(i)<=1000:
        out+=[fact(i)]

fac=lambda num:num in out
print(list(filter(fac,range(1,1001))))