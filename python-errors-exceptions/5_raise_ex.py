#!/usr/bin/python3

#Write a function that raises a type exception.

def raise_ex():
  # Raise a TypeError with a custom message
  raise TypeError("This is a custom TypeError exception") 

if __name__ == "__main__":
  try:
    raise_ex()
  except TypeError as te:
    print("Exception raised: ", te)
