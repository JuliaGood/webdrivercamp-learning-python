#!/usr/bin/python3

# Write a function that adds 2 tuples.
# Returns a tuple with 2 integers:
# The first element should be the addition of the first element of each argument
# The second element should be the addition of the second element of each argument

# If len(tuple) < 2, use the value 0 for each missing integer
# If len(tuple) > 2, use only the first 2 integers

# the default value of 0 will be used for missing elements 
def tuple_addition(first_arg=(0,0), second_arg=(0,0)): 
  
  # Checking and assigning values based on tuple lengths
  first_element_1st_arg = first_arg[0] if len(first_arg) >= 1 else 0
  first_element_2nd_arg = first_arg[1] if len(first_arg) >= 2 else 0

  second_element_1st_arg = second_arg[0] if len(second_arg) >= 1 else 0
  second_element_2nd_arg = second_arg[1] if len(second_arg) >= 2 else 0

  sum_of_1st_elements = first_element_1st_arg + second_element_1st_arg
  sum_of_2nd_elements = first_element_2nd_arg + second_element_2nd_arg

  return (sum_of_1st_elements, sum_of_2nd_elements)
