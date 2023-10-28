#!/usr/bin/python3

original_list = [5, 4, 3, 2, 1]

def boolean_tuple(list_):
  # Create a list of Boolean values indicating if each element in the list is even
  is_even_list = [] # Create an empty list to store Boolean values
  for num in list_:
    # Check if the number is even and append the result to the list (true or false values)
    is_even = num % 2 == 0 
    is_even_list.append(is_even)
  return is_even_list

  # Convert the list of Boolean values into a tuple
  bool_tuple = tuple(is_even_list)
  return bool_tuple

# Print the original list and the created tuple
created_tuple = boolean_tuple(original_list)
print(original_list)
print(created_tuple)
