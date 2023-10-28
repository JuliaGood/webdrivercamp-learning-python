#!/usr/bin/python3

tuple_addition = __import__('7_tuples').tuple_addition

first_arg, second_arg = (1, 99), (-1, 1)
result = tuple_addition(first_arg, second_arg)

print(result)
print(tuple_addition(first_arg, (1, )))
print(tuple_addition((1, 2, 3, 4), (-1, -2, -3, -4)))
print(tuple_addition((), first_arg))
print(tuple_addition())
