#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)

last_digit = abs(random_num) % 10  # Get the last digit

if last_digit == 0:
    print(f"{random_num} - the last digit {last_digit} is zero")
else:
    even_status = "even" if last_digit % 2 == 0 else "odd"
    print(f"{random_num} - the last digit {last_digit} is {even_status}")

