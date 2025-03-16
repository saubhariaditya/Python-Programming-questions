a='python is very easy'.split()
#out=[('python,6'),('is',2),('very',4),('easy',4)]
print([(i,len(i)) for i in a])