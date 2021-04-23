# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration


list_100 = []

a = 1
while a <= 100:
    list_100.append(a)
    a += 1

list_final = []

b = 0
while b < 100:
    if list_100[b] % 7 == 0 and not list_100[b] % 5 == 0:
        list_final.append(list_100[b])
    b += 1

print(f'Конечный результат: {list_final}')
