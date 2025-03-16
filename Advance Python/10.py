a='good morning'.split()
sum=lambda a:len(a)
out=map(sum,a)
print(list(out))


print(list(map(lambda a:len(a),'good morning'.split())))


## a='good morning'
##out= {'good':4, 'morning':7}

sum=lambda a: len(a)
out=map(sum ,a)

print(list(out))
print(dict(map(lambda a:[a,len(a)],a)))

