#Write a program the character is vowel or consonent

char=input("Enter the character: ")
if char in 'AEIOUaeiou':
    print("It contains vowel")
elif char in '0123456789':
    print("Enter a character only")
else:
    print("It is consonent")
