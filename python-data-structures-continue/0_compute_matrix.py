#!/usr/bin/python3

# Write a function that computes the square value of all integers of a matrix.

# 1st way: using .append() method
def compute_matrix_1(matrix=[]):
  computed_matrix = []
  for row in matrix:
    squared_row = []
    for num in row:
      squared_row.append(num ** 2)
    computed_matrix.append(squared_row)
  return computed_matrix

# 2nd way: using the += operator
def compute_matrix_2(matrix=[]):
  computed_matrix = []
  for row in matrix:
    squared_row = []
    for num in row:
      squared_row += [num ** 2]
    computed_matrix += [squared_row]
  return computed_matrix

# 3rd way: using list comprehension
def compute_matrix_3(matrix=[]):
  computed_matrix = [[num**2 for num in row] for row in matrix]
  return computed_matrix
   
if __name__=="__main__":
  matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
  ]
  print(f"Original: {matrix}")
  print(f"Modified 1st way: {compute_matrix_1(matrix)}")
  print(f"Modified 2nd way: {compute_matrix_2(matrix)}")
  print(f"Modified 3rd way: {compute_matrix_3(matrix)}")
