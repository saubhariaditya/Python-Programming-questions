#ANAGRAM::::

a='silent'
b='listen'

a=sorted(a)
b=sorted(b)
print(a)
print(b)
if a==b:
    print('yes the strings are anagram')
else:
    print("not anagram")