#!/usr/bin/python3

num_list = [5, 4, 3, 2, 1]
given_index = 2

def retrieve_element(list_, index):
  if 0 <= index < len(list_):
    element = list_[index]
    print(f"The retrieved element is {element}")
    return element
  else:
    print("Index is negative or out of range.")
    return None

retrieve_element(num_list, given_index)
