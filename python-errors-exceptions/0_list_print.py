#!/usr/bin/python3

# Write a function that prints x elements of a list.
# lst can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.
# i represents the number of elements to print
# i can be bigger than the length of lst
# Returns the real number of elements printed
# You have to use try / except
# You are not allowed to use len()

def list_print(lst=[], i=0): 
  count = 0
  try:
    for element in lst:
      if count < i:
        print(element, end='')
        count += 1
    print()  # New line after printing elements
  except:
    print('Opps, something went wrong!')
  return count


if __name__=="__main__":
  list_ = [1, 2, 3, 4, 5, 6, 7]

  count = list_print(list_, 4)
  print(f"Count: {count:d}")
  count = list_print(list_, len(list_))
  print(f"Count: {count:d}")
  count = list_print(list_, len(list_) + 2)
  print(f"Count: {count:d}")
