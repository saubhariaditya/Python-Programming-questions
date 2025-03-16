#WRITE A PROGRAM TO CHECK PALINDROME STRING:::::::::::::::

a=input("Enter the string: ")
i=1
out=''
while i<=len(a):
    out+=a[-i]
    i+=1
print(out)
if out==a:
    print("Yes it is palindrome")
else:
    print("It is not palindrome")