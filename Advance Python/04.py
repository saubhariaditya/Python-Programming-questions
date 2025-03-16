#WAP TO CHECK THE NUMBER IS EVEN OR ODD, IF THE NUMBER IS EVEN PRINT SQUARE OF IT 
#IF NUMBER IS ODD PRINT CUBE OF IT:::::::

check=lambda a: (a**2) if a%2==0 else (a**3)
print(check(3))