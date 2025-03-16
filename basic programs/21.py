#WAP TO CHECK THE CHARACTER IS SPECIAL CHARACTER OR NOT

char=input('enter the input: ')

#if char in '!@#$%^&*(<>?:+=':

if not ('A'<=char<='a' or 'a'<=char<='z' or '0'<=char<='9'):
    print("Yes it contain special character ")
else:
    print("Not special character")