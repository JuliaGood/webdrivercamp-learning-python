#!/usr/bin/python3

# Write a function that deletes a key in a dictionary.
# key argument will be always a string
# If a key doesn’t exist, the dictionary won’t change

def dict_delete(dict_, key=""):
  if key in dict_:
    del dict_[key]  # Delete the key-value pair if the key exists
  return dict_

if __name__=="__main__":
  dict_print = __import__('6_dict_print').dict_print

  dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java"], "frame": "Behave", "set": set()}
  new_dict = dict_delete(dict_, 'lang')

  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)

  new_dict = dict_delete(dict_, 'y')
  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)
  