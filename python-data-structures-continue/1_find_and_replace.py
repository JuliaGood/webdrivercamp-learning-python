#!/usr/bin/python3

# Write a function that replaces all occurrences of an element by another in a new list.

# original is the list
# find is the element to replace
# replace is the replacement 

# 1st way: using .append() method
def find_replace_1(original, find, replace):
  new_list = []
  for num in original:
    if num == find:
      num = replace 
    new_list.append(num)
  return new_list

# 2nd way: using the += operator
def find_replace_2(original, find, replace):
  new_list = []
  for num in original:
    if num == find:
      num = replace 
    new_list += [num]
  return new_list

# 3rd way: using list comprehension 
def find_replace_3(original, find, replace):
  new_list = [replace if num == find else num for num in original]
  return new_list

if __name__=="__main__":
  original = [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
  modified1 = find_replace_1(original, 9, 13)
  modified2 = find_replace_2(original, 9, 13)
  modified3 = find_replace_3(original, 9, 13)

  print(f"Original : {original}")
  print(f"Modified1: {modified1}")

  print(f"Original : {original}")
  print(f"Modified2: {modified2}")

  print(f"Original : {original}")
  print(f"Modified3: {modified3}")
