#WAP TO FIND THE VOWELS IN THE STRING AND COUNT ALSO

a=(input("Enter the String: "))
out=''
c=0
i=0
while i<len(a):
    if a[i] in 'AEIOUaeiou':
        out+=a[i]
        c+=1
    i+=1
print(out,c)