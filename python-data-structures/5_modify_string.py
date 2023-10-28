#!/usr/bin/python3

given_string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
  # Add your code to remove all characters 'a' (both lower and upper) from the string
  new_string = ''
  for char in some_string:
    if char not in 'Aa': # The 'not in' operator is used to check if a value is not present in a sequence 
      new_string += char # new_string = new_string + char
  return new_string

modified_string = remove_char(given_string)
print(modified_string)
