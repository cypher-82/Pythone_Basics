# Quadratic Equation Discriminant Calculator
# ax^2 + bx + c = 0 : Quardatic Equation
# b^2 - 4(ac) : Discriminant Formula

print(f'The equation is ax^2 + bx + c = 0 :')

a = int(input("Value of a = "))
b = int(input("Value of b = "))
c = int(input("Value of c = "))

dis = b**2 - 4*(a*c)

print(f'The Discriminant of Quardatic Equation is : {dis}')
