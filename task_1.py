#!/usr/bin/env python3

year = int(input('Enter year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Is intercalary: Yes')
else:
    print('Is intercalary: No')
