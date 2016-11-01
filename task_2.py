#!/usr/bin/env python3

number1 = int(input('Please enter first number: '))
number2 = int(input('Please enter second number: '))
number3 = int(input('Please enter third: '))

if number1 == number2 == number3:
    print('Result: 3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('Result: 2')
else:
    print('Result: 0')
