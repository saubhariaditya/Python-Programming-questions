a='aeroplane'
op=[('a',2),('o',1),('e',2)]

print([(i,a.count(i)) if i in ['a','e','i','o','u']  else '' for i in a])


