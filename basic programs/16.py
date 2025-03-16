#WAP to check the num is divisible by 5 and 7

a=int(input("Enter the number: "))

if a%5==0:
    print("It is divisible by 5")
elif a%7==0:
    print("It is divisible by 7")
else:
    print("Not divisible")