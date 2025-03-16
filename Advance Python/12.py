a='good morning'.split()
sum=lambda a: a.upper()
out=map(sum ,a)
print(dict(map(lambda a:[a, a.upper()],a)))
