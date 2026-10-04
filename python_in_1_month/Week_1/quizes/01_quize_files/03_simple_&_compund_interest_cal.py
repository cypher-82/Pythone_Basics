# Simple and Compund Interest Calculator
# SI = (P * R * T) / 100
# CI = P * (1 + R/100) ** T - P
# P=Principle(Amount) , R=Rate(%) , T=Time(Years, Months)

P = float(input("Enter Principle (Amount) : "))
R = float(input("Enter Rate (Percentage) : "))

sel_var = input('How would you like to add time, Month or Years (m/y) : ')

if sel_var == 'm':
    T_m = float(input("Enter Time (Months) : "))
    T_m = T_m / 12
    SI = (P * R * T_m) / 100 # Simple Interest
    CI = P * (1 + R/100) ** T_m - P # Compund Interest
    
    print("-----------------------------------------------------------------------------------")

    print(f'So the Amount is {P:.2f} in Rate of {R}% will be in Time {T_m:.2f} years The SI and CI will:')
    print(f"Simple Interest is = {SI:.2f}")
    print(f"Compund Interest is = {CI:.2f}")

    print('|||||||||||||||||||||||||||||||||||')

    difference = CI - SI
    print(f"CI is {difference:.2f} more then SI in {T_m:.2f} years.")
else:
    T = float(input("Enter Time (Years) : "))
    SI = (P * R * T) / 100 # Simple Interest
    CI = P * (1 + R/100) ** T - P # Compund Interest

    print("-----------------------------------------------------------------------------------")
    
    print(f'So the Amount is {P:.2f} in Rate of {R}% will be in Time {T:.2f} years The SI and CI will:')
    print(f"Simple Interest is = {SI:.2f}")
    print(f"Compund Interest is = {CI:.2f}")
    
    print('|||||||||||||||||||||||||||||||||||')
    
    difference = CI - SI
    print(f"CI is {difference:.2f} more then SI in {T:.2f} years.")