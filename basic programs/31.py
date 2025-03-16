#WAP TO PRINT A NUMBER WHICH ID DIVISIBLE BY 5 BUT IT SHOULD BE EVEN NUMBER:

a=int(input("Enter the number: "))
if a%5==0:
    if(a%2==0):
        print("Yes it is divisible by 5 and even")
    else: 
        print("Divisible by 5 but odd")
else:
    print("Not divisible by 5")




