def perfect(a,i=1,out=0):
    if i>=a:
        return out
    if a%i==0:
        out+=i
    return perfect(a,i+1,out)
a = 6
res = perfect(a)

if a == res:
    print("Perfect number")
else:
    print("Not perfect number")

