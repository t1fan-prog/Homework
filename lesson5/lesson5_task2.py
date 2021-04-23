# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers

import random


def randomizer(some_list):
    a = 0
    while a < 10:
        rand_int = random.randint(1, 10)
        some_list.append(rand_int)
        a += 1


list_1 = []
randomizer(list_1)

list_2 = []
randomizer(list_2)

list_common = list(set(list_1) & set(list_2))

print(f'First list: {list_1}', f'Second list: {list_2}', f'Common list: {list_common}', sep="\n")
