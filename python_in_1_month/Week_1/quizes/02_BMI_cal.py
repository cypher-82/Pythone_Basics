# BMI ( Body Mass Index ) Calculator
# BMI = weight(kg) / (height(meter) ** 2)

weight = float(input("Weight in (Kg): "))
height = float(input("Height in (cm): "))

print('----------------------------------------------------------------')

print(f'''your weight is {weight}kg and height is {height}cm
accourding to this data your BMI is: ''')

height = height / 100 # 170cm into 1.70m
your_bmi = weight / (height ** 2)

print(f"{your_bmi:.2f}") 
