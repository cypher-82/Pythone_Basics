# A leap year is a year that has 366 days instead of the usual 365 days.
# To find out if a specific year is a leap year, you apply these three rules:
# 1. The year must be evenly divisible by 4.
# 2. If the year can also be evenly divisible by 100, it is NOT a leap year...
# 3. ...UNLESS the year is also evenly divisible by 400

leap_year = int(input('Enter the year (YYYY) : '))

if leap_year % 400 == 0 and (leap_year % 4 == 0 or leap_year % 100 != 0):
    print(f'{leap_year} is a Leap Year.')
else:
    print(f'{leap_year} is not a Leap Year.')