#!/usr/bin/python3

#Write a function that adds all unique integers in a list (only once for each integer).

def only_unique(list_=[]):
  new_set = set(list_)
  total_sum = 0

  for num in new_set:
    total_sum += num

  print(new_set)
  return total_sum
  
if __name__=="__main__":
  list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
  result = only_unique(list_)
  print(f"Sum of unique: {result}")
