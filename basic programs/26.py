#Write a program to print the character is uppercase print upper if lower then print lower. if it is number print number
#if it is special character print char
#if your character is upper case print same char, if it is lower print uppercase, if it is number print cobe of it, if it is special character print special character with message

a=(input("Enter the input: "))
if 'A'<=a<='Z':
    print("Uppercase",)
elif 'a'<=a<='z':
    print("lowercase")
elif '0'<=a<='99999999999999':
    print("Number")
elif a in '!@#$%^&*(<>?:+=':
    print("Special character")
else:
    print("Enter correct input")