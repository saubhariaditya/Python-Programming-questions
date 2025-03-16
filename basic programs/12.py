#TO CHECK THE COLLECTION IS MULTIVALUE DATATYPE AND IT'S LENGTH IS SHOULD BE MORE THAN 5

a=eval(input("Enter the collection: "))
print(a)
print(type(a))

b=(len(a))

#if type(a) == str or type(a)== list or type(a)== tuple or type(a)==set  and b>=5:
if type(a) in [str,list,tuple,set,dict] and b>5:
    print("The given collection is multi valued datatype ") 
else:
    print("It is not accepted")