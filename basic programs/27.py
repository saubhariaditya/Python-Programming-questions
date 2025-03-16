'''if your character is upper case print same char, 
if it is lower print upper, if it is number print cobe of it, 
if it is special character print special character with message
'''

a=(input("Enter the input: "))

if 'A'<=a<='Z':
    print(a)
elif 'a'<=a<='z':
    print("lower")
elif '0'<=a<='99999999999999':
    print(int(a)**3)
elif a in '!@#$%^&*(<>?:+=':
    print("Special character", a)
else:
    print("Enter correct input")
