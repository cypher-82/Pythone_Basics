num_1 = int(input("Enter number : "))
operator = input('Enter the operator One of these (+,-,*,/,//,%,**) : ')
num_2 = int(input("Enter second number : "))

print('--------------------------------------------------------------')


if operator == '+':
    print(f"The sum is = {num_1 + num_2}")
elif operator == '-':
    print(f"The sub is = {num_1 - num_2}")
elif operator == '*':
    print(f"The mul is = {num_1 * num_2}")
elif operator == '/':
    print(f"The div is = {num_1 / num_2}")
elif operator == '//':
    print(f"The floor div is = {num_1 // num_2}")
elif operator == '%':
    print(f"The modulus is = {num_1 % num_2}")
elif operator == '**':
    print(f"The power is = {num_1 ** num_2}")
elif operator == '-+*///%**':
    print("Please select only one operator!")
else:
    print('Please Slect operator first!')
    