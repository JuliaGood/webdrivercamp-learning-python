#!/usr/bin/python3

# list_1 and list_2 can contain any type (integer, string, etc.)
# list_len can be bigger than the length of both lists
# Returns a new list (length = list_len) with all divisions
# If 2 elements can’t be divided, the division result should be equal to 0
# If an element is not an integer or float:
# print: wrong type
# If the division can’t be done:
# print: division by 0
# If list_1 or list_2 is too short
# print: out of range
# You have to use try / except / finally


def divide_list_safe(list_1, list_2, list_len):
  result = [] # Create an empty list to store division results
  
  for i in range(list_len):  # Iterate through the lists up to list_len
    try:
      # If i is greater than or equal to the length of lists, it means that lists don't have an element at the current index i.
      if i >= len(list_1) or i >= len(list_2):    
        raise IndexError("out of range") 
      
      num1 = float(list_1[i])
      num2 = float(list_2[i]) # Convert the element of lists to a float

      if num2 == 0:
        raise ZeroDivisionError("division by 0")

      division_result = num1 / num2
      result.append(division_result)

    except ValueError:
      print("wrong type")
      result.append(0)
    except ZeroDivisionError:
      print("division by 0")
      result.append(0)
    except IndexError as err:
      print(err)
      result.append(0)
  
  return result


if __name__ == "__main__":
  list_1 = [9, 2, 6]
  list_2 = [3, 2, 2]
  res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
  print(res)
  print(10*"_")
  print()

  list_1 = [9, 2, 6, 10]
  list_2 = ["one", 0, 1, 2, 7]
  res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
  print(res)
