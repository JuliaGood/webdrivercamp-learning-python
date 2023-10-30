#!/usr/bin/python3

# Write a function that returns a new dictionary with all values multiplied by 2
# using .items() method
def mult_values(dict_):
  new_dict = {}
  dict_items = dict_.items()
  print(f"dict_items:\n{dict_items}")
  for key, val in dict_items:
    new_dict[key] = val * 2
  return new_dict

if __name__=="__main__":
  dict_print = __import__('6_dict_print').dict_print

  dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
  new_dict = mult_values(dict_)
  dict_print(new_dict)
