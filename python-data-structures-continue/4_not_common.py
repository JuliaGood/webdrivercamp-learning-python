#!/usr/bin/python3

# Write a function that returns a set of all elements present in only one set.

# 1st way: using .symmetric_difference() method 
def not_common_elements_1(a, b):
  result = a.symmetric_difference(b)
  return result

# 2nd way: using ^ operator
def not_common_elements_2(a, b):
  result = a ^ b
  return result

if __name__=="__main__":
  set_a = {"API", "requests", "Selenium", "Python", "Behave"}
  set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}

  elements_1 = not_common_elements_1(set_a, set_b)
  [print(x) for x in sorted(list(elements_1))]

  elements_2 = not_common_elements_2(set_a, set_b)
  [print(x) for x in sorted(list(elements_2))]
