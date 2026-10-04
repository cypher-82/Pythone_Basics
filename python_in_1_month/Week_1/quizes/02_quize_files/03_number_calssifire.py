# How to check tha integer number is even or odd.

n = int(input('Enter an integer number acpect 0 : '))

# For Check it Even or Odd
if n % 2 == 0:
    print(f'{n} is Even number')
elif n % 2 == 1:
    print(f'{n} is Odd number')