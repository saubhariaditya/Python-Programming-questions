#WAP TO CHECK THE DATA IS SINGLE VALUE DATA TYPE THEN PRINT 1 OTHERWISE LEN OF THE DATA::::::

a=lambda a:1 if type(a) in [int,float,complex,bool] else len(a)
print(a(2))


a='abcbsbahks'
print(a.find('s'))

