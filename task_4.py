#!/usr/bin/env python3

list = input('Enter list numbers: ')
list = list.split(' ')
count = 0

for index in list:
    if list.count(index) >= 2:
        index = 1
        count += index
print(count / 2)