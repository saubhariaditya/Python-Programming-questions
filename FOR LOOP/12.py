a=23
while True:
    num=int(input("Enter the number: "))
    if num==a:
        print("Congrats you won: ")
        break
    elif num>a:
        print("Better luck for next time")
    else:
        print("You LOST ")
        