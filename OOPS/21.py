#### MULTIPLE INHERITANCE ######
import string
class alphabet:
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
class number:
    num='1,2,3,4,5,6,7,8,9,0'
class special:
    special='!,@,#,$,%,^,&,*,(,),?,<,>,'
class char(alphabet, number,special):
    pass

print(char.lower, char.upper, char.num, char.special)
