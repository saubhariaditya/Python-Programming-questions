#WAP PRINT ALL THE EVEN NUMBERS PRESENT IN THE RANGE 1 TO 100:::

even=lambda num:num%2==0
out=filter(even,range(1,101))   
print(list(out))     

