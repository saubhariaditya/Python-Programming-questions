#WAP TP PRINT FACTORIAL OF A NUMBER PRESENT INSIDE NUMBERLIST:::::::
#import math
#a=[1,3,4,5,6]
#out=[]
#for i in a:
#       if i==0:
#        out+=0
#       else:
#          out+= math.factorial(i)
#print(out)


def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(list(map(fact,[1,22,3,4,5])))
    
