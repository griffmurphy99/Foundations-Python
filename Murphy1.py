from math import pi #imports the number for pi
r = float(input ("Input the radius of the circle : ")) #ask user to input the radius

print ("The circumference of a circle with a radius of " + str(r) + " is: " + str(2 * pi * r)) #calculates circumference using formula

print ("The area of a circle with a radius of " + str(r) + " is: " + str(pi * r**2)) #calculates area using formula

print ("The volume of a sphere with a radius of " + str(r) + " is: " + str((4/3) * pi * r**3)) #calculates volume using formula
