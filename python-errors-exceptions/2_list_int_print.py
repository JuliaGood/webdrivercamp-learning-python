#!/usr/bin/python3

# Write a function that prints the first i elements of a list and only integers.
# lst can contain any type (integer, string, etc.)
# All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
# i represents the number of elements to access in lst
# if i is bigger than the length of lst - an exception is expected to occur
# Returns the real number of integers printed
# You have to use try / except
# You have to use f"{integer:d}" to print an integer
# You are not allowed to use len()


def list_int_print(lst=[], i=0):
  count = 0
  try:
    for x in range(i):
      value = lst[x]
      if isinstance(value, int): #check if the value is an integer
        print(f"{value:d}", end="")
        count += 1
    print()
  except IndexError:
    raise Exception("i is bigger than the length of lst")
  return count

if __name__=="__main__":
  list_ = [1, 2, 3, 4, 5, 6, 7]

  count = list_int_print(list_, 4)
  print(f"Count: {count:d}")

  list_ = [1, 2, "Camp", 5, [3, 4]]
  count = list_int_print(list_, len(list_))
  print(f"Count: {count:d}")
  count = list_int_print(list_, len(list_) + 2)
  print(f"Count: {count:d}")
