#Write a program to check two strings if len of 1st string is greater
#than 2nd string then do concat of 2 strings other wise product of 1st string with len of 2nd string


a=input("Enter the String: ")
b=input("Enter the second String: ")

if len(a)>len(b):
    print(a+b)
else:
    print(a*len(b))