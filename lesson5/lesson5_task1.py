# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

import random

random_list = []
a = 0

while a < 10:
    rand_int = random.randint(0, 1000)
    random_list.append(rand_int)
    a += 1

max_int = max(random_list)
print(random_list, f'The largest number is {max_int}', sep="\n")
