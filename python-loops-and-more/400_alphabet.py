#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in 'aq':
        print(chr(letter), end='')

print('$', end='')  # Print the $ character without a newline 


