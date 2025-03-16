#Write a program to find the area and parameter of rectangle, square and circle

print(" AREA AND PARAMATER OF SQUARE")
a=int(input("Enter the length of side of the square: "))
print("Area of the square is: ",a*a)
print("Paramter of the square is: ",4*a)

print("AREA AND PARAMATER OF RECTANGLE")
b=int(input("Enter the length of the rectangle: "))
c=int(input("Enter the breath of the rectangle: "))
print("Area of rectangle is: ", 2*b*c)
print("Paramater of rectangle is: ", 2(b+c))

print("AREA and paramater of circle")
r=float("Enter the radius of the circle: ")
p=3.14
print("Area of the circle is: ", p*r**2 )
print("paramater of the circle is", 2*p*r)