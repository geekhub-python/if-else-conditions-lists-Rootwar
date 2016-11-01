#!/usr/bin/env python3

rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))
quantity_cake = int(input('Enter quantity cake: '))

if rows * columns > quantity_cake and quantity_cake % rows == 0 or quantity_cake % columns == 0:
    print('Result: Yes')
else:
    print('Result: No')