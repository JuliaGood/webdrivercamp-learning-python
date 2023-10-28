#!/usr/bin/python3

#Write a function that returns a tuple with the length of the list and its first element
#Prototype: def tuple_return(arg):
#If the list is empty, the first element should be equal to None

def tuple_return(arg):
  if len(arg) == 0:  # Check if the list is empty
  # if not arg:  # 2nd way to check if the list is empty
    return (len(arg), None)
  else:
    return (len(arg), arg[0])
