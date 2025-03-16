'''WRITE A PROGRAM THE NUM IS DIVISIBLE BY 3 PRINT FIZZ, IF IT IS DIVISIBLE BY 5 PRINT BUZZ
FOR BOTH FIZZBUZZ'''
a=int(input("Enter the input: "))

if a%3==0 and a%5==0:
    print("FIZZBUZZ")
elif a%5==0:
    print("BUZZ")
elif a%3==0:
    print("FIZZ")
else:
    ("okay")