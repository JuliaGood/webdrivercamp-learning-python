#!/usr/bin/python3

# Safe division. Write a function that divides 2 integers and prints the result.
# The result of the division should print on the finally: section preceded by Result: 
# Returns the value of the division, otherwise: None
# You have to use try / except / finally

def divide_safe(a, b):
  try:
    result = a / b
  except ZeroDivisionError as err:
    print(f"{err}")
    result = None
  finally:
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
  a = 9
  b = 3
  result = divide_safe(a, b)
  print(f"{a} / {b} = {result}")

  b = 0
  result = divide_safe(a, b)
  print(f"{a} / {b} = {result}")
