# Grade Calculation program

total_marks = float(input('Enter Total Marks : '))
obtained_marks = float(input("Enter Obtained Marks : "))

grade = (obtained_marks / total_marks) * 100

if grade <= 0:
    print('0 is not allowed to be divisor!')
elif grade > 100:
    print('Invailed Input! please re-enter!')
elif grade >= 90:
    print(f'You\'re grade is {grade:.2f}% : A+')
elif grade >= 80:
    print(f'You\'re grade is {grade:.2f}% : A')
elif grade >= 70:
    print(f'You\'re grade is {grade:.2f}% : B')
elif grade >= 60:
    print(f'You\'re grade is {grade:.2f}% : C')
elif grade >= 50:
    print(f'You\'re grade is {grade:.2f}% : D')
else:
    print('Your are Fail!')