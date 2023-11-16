#!/usr/bin/python3

# Write a function that prints an integer (f"{value:d}")
# value can be any type (integer, string, etc.
# The integer should be printed followed by a new line
# Returns True if value was printed else False
# You have to use try / except
# You are not allowed to use type()

def int_print(val):
  try:
    print(f"{int(val):d}")
    return True
  except (ValueError, TypeError):
    return False
  
if __name__ == "__main__":
  value = 42
  if not (int_print(value)):
    print(f"{value} is not an integer")

  value = -100
  if not (int_print(value)):
    print(f"{value} is not an integer")

  value = "Webdriver Camp"
  if not (int_print(value)):
    print(f"{value} is not an integer")
