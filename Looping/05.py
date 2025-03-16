#WAP TO PRINT NUMBER IS DIVISIBLE BY 5 FROM M TO N :
m=0
n=int(input("Enter the number: "))
while m<=n:
    if m%5==0:
        print(m)
    m+=1