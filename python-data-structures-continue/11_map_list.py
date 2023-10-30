#!/usr/bin/python3

# Write a function that returns a list with all values multiplied by a number without using any loops.
# Returns a new list:
# Same length as the original
# Each value should be multiplied by number

def map_list(list_=[], num=0):
  new_list = []
  for item in list_:
    new_list.append(item * num)
  return new_list

def map_list_2(list_=[], num=0):
  return list(map(lambda x: x * num, list_))

if __name__=="__main__":
  list_ = [5, 4, 3, 2, 1, 7]
  new_list = map_list(list_, 4)
  new_list2 = map_list_2(list_, 4)

    
  print(f"Original: {list_}")
  print(f"Modified: {new_list}")
  print(f"Modified: {new_list2}")
