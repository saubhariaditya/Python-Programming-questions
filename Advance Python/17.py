#PRint all even number from 1 to 100 inside a list::::


out=[]
for i in range(1,100):    ## NORMAL ##
    if i%2==0:
        out+=[i]
print(out)




num=[i for i in range(1,100,) if i%2==0]
print(num)                                           ## BY USING COMPREHENSION ##