#!/usr/bin/python3

# Write a function that deletes keys with a specific value in a dictionary.
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted

def dict_v_delete(a_dictionary, value):

  keys_to_delete = []
  # Finding keys with the specified value
  for key, val in a_dictionary.items():
    if val == value:
      keys_to_delete.append(key)

  # Deleting keys with the specified value
  for key in keys_to_delete:
    del a_dictionary[key]

  return a_dictionary


if __name__=="__main__":
  dict_print = __import__('6_dict_print').dict_print

  dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java"], "frame": "Selenium"}
  new_dict = dict_v_delete(dict_, "Selenium")

  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)

  new_dict = dict_v_delete(dict_, 'y')
  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)