#!/usr/bin/python3

original_list = [5, 4, 3, 2, 1]
# Create a tuple with True or False values depending 
# if the element at the same index in the list is even or odd

def boolean_tuple(list_):
  new_tuple = () # create an empty tuple
  for num in list_:
    # create a one-element tuple, and check whether num is even.
    # num is divided by 2. If the remainder is 0, it means that num is even.
    # 'true' if num is even, and 'false' if num is odd.
    is_even = (num % 2 == 0, ) # comma is essential to create a single-element tuple!
    #The comma after the expression ensures it's treated as a tuple even if it contains just one element.
    new_tuple += is_even
  return new_tuple

# Print the original list and the created tuple
created_tuple = boolean_tuple(original_list)
print(original_list)
print(created_tuple)
