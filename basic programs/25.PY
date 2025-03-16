#WAP TO CHECK THE NUMBER IS 1,2,3,4 DIGIT

num=int(input("Enter the number : "))
if 0<=num<=9:
    print('1 digit number')
elif 10<=num<=99:
    print('2 digit number')
elif 100<=num<=999:
    print('3 digit number')
elif 1000<=num<=9999:
    print('4 digit number')
else:
    print("OK")