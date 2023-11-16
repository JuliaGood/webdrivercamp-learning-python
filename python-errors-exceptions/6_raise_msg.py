#!/usr/bin/python3

# Write a function that raises a name exception with a message.

def raise_message(message=""):
  # Raise a NameError with a custom message
  raise NameError(message)
  
if __name__ == "__main__":
  try:
    raise_message("I love Python!")
  except NameError as ne:
    print(ne)
