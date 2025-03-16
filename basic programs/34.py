#WAP TO CREATE LOGIN CRIDENTIAL
print("Sign up")
a=(input("Enter username to create account: "))
b=(input("Enter password to create account: "))
print("Sign up successful")

c=(input("Enter your username again to login: "))
d=(input("Enter your password to login: "))

if a==c:
    print("your username is correct ")
    if b==d:
        print("Your password is correct")
    else:
        print("Your password is incorrect")
    print("Welcome ")
else:
    print("Please enter correct details")
