#!/usr/bin/python3

# Write a function that returns a set of common elements in two sets.

# 1st way: using .intersection() method 
def common_elements_1(a, b):
  result = a.intersection(b)
  return result

# 2nd way: using intersection & operator
def common_elements_2(a, b):
  result = a & b
  return result

if __name__=="__main__":
  set_a = { "API", "requests", "Selenium", "Python", "Behave"}
  set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}

  same_element_1 = common_elements_1(set_a, set_b)
  [print(x) for x in sorted(list(same_element_1))]

  same_element_2 = common_elements_2(set_a, set_b)
  [print(x) for x in sorted(list(same_element_2))]
