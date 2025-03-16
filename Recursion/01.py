#To find limit of recursion::::::::::::::::::::::::::::::::::::::
import sys
print(sys.getrecursionlimit())




#WE CAN INCREASE LIMIT OF RECURSION::::::
print(sys.setrecursionlimit(2000))


#WAP TO FIND THE FACTORIAL OF A NUMBER::::::::::::::::::::::

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(1111))

def fact(a):
    for i in a:
        if i==0 or i==1:
            return 1
        return i*fact(i-1)
print(fact([1,2,3,4,5,6,7,8,9]))



