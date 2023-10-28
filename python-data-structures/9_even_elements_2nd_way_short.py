#!/usr/bin/python3

original_list = [5, 4, 3, 2, 1]

def boolean_tuple(list_):
  # Create a list of Boolean values indicating if each element in the list is even
  is_even_list = [num % 2 == 0 for num in list_]
  return is_even_list

  # Convert the list of Boolean values into a tuple
  bool_tuple = tuple(is_even_list)
  return bool_tuple

# Print the original list and the created tuple
created_tuple = boolean_tuple(original_list)
print(original_list)
print(created_tuple)
