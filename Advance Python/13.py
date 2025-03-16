### Fibonacci series between 1 to 100 with the help of filter:::::

def fib(n):
    out=[]
    a,b=0,1
    while a<n:
        print(a, end= ' ')
        a,b=b,a+b
    out+=[a]
fib(1000)

