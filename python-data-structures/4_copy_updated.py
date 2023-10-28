#!/usr/bin/python3

num_list = [5, 4, 3, 2, 1]
given_index = 1
element_to_replace = 5

def replace_element_1(list_, index, element):
  if 0 <= index < len(list_): 
    # Create a copy of the original list using list() function
    copied_list = list(list_)  
    copied_list[index] = element
  print(f"copied list 1: {copied_list} ")
  print(f"original list: {num_list} ")

def replace_element_2(list_, index, element):
  if 0 <= index < len(list_): 
    # Create a copy of the original list using list slicing
    copied_list = list_[:]  
    copied_list[index] = element
  print(f"copied list 2: {copied_list} ")
  print(f"original list: {num_list} ")

def replace_element_3(list_, index, element):
  if 0 <= index < len(list_): 
    # Create a copy of the original list using .copy() method
    copied_list = list_.copy()  
    copied_list[index] = element
  print(f"copied list 3: {copied_list} ")
  print(f"original list: {num_list} ")

def replace_element_4(list_, index, element):
  if 0 <= index < len(list_): 
    # Create a copy of the original list using * operator to unpack a list
    copied_list = [*list_]  
    copied_list[index] = element
  print(f"copied list 4: {copied_list} ")
  print(f"original list: {num_list} ")


print('replaced element in list using 1st way: ')
replace_element_1(num_list, given_index, element_to_replace)

print('replaced element in list using 2nd way: ')
replace_element_2(num_list, given_index, element_to_replace)

print('replaced element in list using 3rd way: ')
replace_element_3(num_list, given_index, element_to_replace)

print('replaced element in list using 4th way: ')
replace_element_4(num_list, given_index, element_to_replace)
