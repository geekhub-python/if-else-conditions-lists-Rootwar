#!/usr/bin/env python3

list = input('Enter list numbers: ')
list = list.split(' ')
count = 0

for index in list:
    count += list.count(index)
print('Result:', (count - len(list)) // 2)
