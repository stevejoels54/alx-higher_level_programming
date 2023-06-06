#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10 if number > 0 else (abs(number) % 10) * -1
print(f"Last digit of {number:d} ", end="")
if (lastdigit > 5):
    print(f"is {lastdigit:d} and is greater than 5")
elif (lastdigit < 6 and lastdigit != 0):
    print(f"is {lastdigit:d} and is less than 6 and not 0")
elif (lastdigit == 0):
    print(f"is {lastdigit:d} and is 0")
