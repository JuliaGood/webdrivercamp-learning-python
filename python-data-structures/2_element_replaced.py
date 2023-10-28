#!/usr/bin/python3

num_list = [5, 4, 3, 2, 1]
given_index = 1
element_to_replace = 5

def replace_element(list_, index, element):
  if 0 <= index < len(list_): # if index is within the valid range
  # the 2nd way to check if index is within the valid range ->
  # if index in range(len(list_)): 
    list_[index] = element
  print(list_)

replace_element(num_list, given_index, element_to_replace)
