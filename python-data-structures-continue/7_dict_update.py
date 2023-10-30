#!/usr/bin/python3

# Write a function that replaces or adds key/value in a dictionary.
# key argument will be always a string
# value argument will be any type
# If a key exists in the dictionary, the value will be replaced
# If a key doesn’t exist in the dictionary, it will be created

def dict_update(dict_, key, value):
  new_dict = dict_.copy()  # Create a copy of the original dictionary
  new_dict[key] = value  # Update or add the key-value pair in the new dictionary
  return new_dict

if __name__=="__main__":
  dict_print = __import__('6_dict_print').dict_print

  dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java"], "frame": "Behave", "set": set()}
  new_dict = dict_update(dict_, 'lang', "Python")

  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)

  new_dict = dict_update(dict_, 'stars', 5)
  print(f"{'Updated Dict':.^20}")
  dict_print(new_dict)
