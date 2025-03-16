# WAP TO FIND THE SUM OF NUMBERS PRESENT IN YOUR EMAIL ID::::

def sum_num(a):
    sum=0
    for i in a:
        if '0'<=i<='9':
            sum+=int(i)
    print(sum)
sum_num('aditya121@gmail.com')
