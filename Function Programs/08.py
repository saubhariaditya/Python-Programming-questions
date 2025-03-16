#WAP TO EXTRACT ALL THE INTEGER FROM THE GIVEN LIST WHICH ARE PALINDROME IN NATURE AND PRESENT AT EVEN INDEX.
def find_palindrome(a):
    a=[1221,2,'hello',000,5+4j,3223,'hai']
    out=[]
    for i in range (0,len(a),2):
        if (type(a[i]==int and i%2==0)):
            if str(a[i])==str(a[i])[::-1]:
                out+=[a[i]]
    print(out)
find_palindrome([1221,2,'hello',000,5+4j,3223,'hai'])
