#!/usr/bin/python3

# Write a function that returns the weighted average of all integers tuple (<score>, <weight>)
# Returns 0 if the list is empty

def calc_weight(list_=[]):
  if len(list_) == 0:  # if not list_: 
    return 0

  # Initialize variables to store the total multiplied values and total weights
  weighted_sum = 0
  total_weight = 0

  # Iterate through each tuple in the list
  for score, weight in list_:
    # Multiply the score by its weight and add it to the total multiplied values
    weighted_sum += score * weight
    # Add the weight to the total weights
    total_weight += weight

  # Check if the total weight is zero to avoid division by zero
  if total_weight == 0:
    return 0

  # Calculate the weighted average by dividing the total multiplied values by the total weights
  return weighted_sum / total_weight

if __name__=="__main__":
  list_ = [(3, 2), (5, 9), (7, 7)]
  # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
  result = calc_weight(list_)
  print(f"Weight: {result:0.2f}")
