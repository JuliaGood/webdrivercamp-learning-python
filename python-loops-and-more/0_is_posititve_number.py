#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
#ADD YOUR CODE HERE
if random_num > 0:
    status = "is positive"
elif random_num < 0:
    status = "is negative"
else:
    status = "is zero"

print(f"{random_num} {status}")


