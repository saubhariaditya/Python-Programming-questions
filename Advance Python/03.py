#WAP TO CHECK THE LENGTH OF FIRST STRING GREATER THEN SECOND STRING IF FIRST IS GREATER THEN SECOND
# PRINT PYTHON IS EASY OTHERWISE PYTHON IS HARD:::::

def gre(a,b):
    if len(a)>len(b):
        return 'Python is easy'
    return 'Python is hard'
print(gre('elephant','hoppotomous'))

###############################################################################################
check=lambda a,b: 'python is easy' if len(a)>len(b) else 'python is hard'
print(check('elephant', 'gorilla'))