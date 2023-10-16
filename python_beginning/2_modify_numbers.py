#!/usr/bin/python3
number = 3.141592653589793238

# f-string format
print(f'Learning Python is fun\"\' - {number:.2f} % ')

# .format() method
print('Learning Python is fun\"\' - {:.2f} %'.format(number))

# % operator
print('Learning Python is fun\"\' - %.2f %%' % number)

