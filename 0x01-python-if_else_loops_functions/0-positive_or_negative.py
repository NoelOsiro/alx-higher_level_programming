#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Check the value of 'number' and print the appropriate message
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
