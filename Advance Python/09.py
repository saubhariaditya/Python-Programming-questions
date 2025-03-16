#########################____MAPPING____#########################
#WAP TO FIND THE SQUARE OF A VALUE PRESENT IN RANGE 1-10

sqr=lambda num:num**2   #by lambda
out=map(sqr,range(1,10))
print(list(out))


print(list(map(lambda num:num**2,range(1,10))))  ## IN one line