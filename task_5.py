#!/usr/bin/env python3

list = input('Enter list numbers: ')
list = list.split(' ')

for index in range(len(list)):
    number = int(list[index])
    next_number = int(list[index + 1])
    if number > 0 and next_number > 0 or number < 0 and next_number < 0:
        print(list[index], list[index + 1])
        break