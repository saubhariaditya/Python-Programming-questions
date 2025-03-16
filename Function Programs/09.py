def str_palindrome(a):
    a='Hiee nitin to ava'.split()      
    out=''
    for i in range (len(a)):
        if a[i]==a[i][::-1]:
            out+=a[i]
            out+=' '
    print(out)
str_palindrome('hiee nitin to ava'.split())
