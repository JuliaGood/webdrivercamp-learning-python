#!/usr/bin/python3

# Write a function that returns a key with the biggest integer value.
# You can assume that all values are only integers
# If no score found, return None

def max_value(d):
  if d is None or not d: # d is either None or empty. 
    return None

  biggest_key = None

  for key, val in d.items():
    if biggest_key == None:
      biggest_key = key
    elif val > d.get(biggest_key):
      biggest_key = key
  return biggest_key

if __name__=="__main__":
  dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
  max_key = max_value(dict_)
  print(f"Max number - {max_key}")

  max_key = max_value(None)
  print(f"Max number - {max_key}")
  