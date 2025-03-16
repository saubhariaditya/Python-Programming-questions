def fact_list(l,i=0,out=[]):
    def fact(n):
        if n==1 or n==0:
            return 1
        else:
            return n*fact(n-1)
    if i>=len(l):
        return out
    else:
        out.append(fact(l[i]))
    return fact_list(l,i+1,out)
print(fact_list([1,2,3,4,5,6,7,8,9,10]))