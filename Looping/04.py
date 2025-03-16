#WAP TO CHECK NUMBER IS DIVISIBLE BY 5 limit 1 to 100:
num = int(input("Enter a number: "))
if num<=100:
    if num%5==0:
        print("Yes it is divisible by 5")
    else:
        print("No it is not divisible by 5")
else:
    print("Enter number between 1 to 100 ")
