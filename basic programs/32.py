#WAP TO CHECK THE CHARACTER IS VOWLE OR NOT:
char=input("Enter the character: ")

if 'A'<=char<='Z' or 'a'<=char<='z':
    if char in 'AEIOUaeiou':
        print("Yes it contains vowle ")
    else:
        print("Consonant")
else:
    print("It is not a string")