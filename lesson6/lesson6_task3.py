# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding
# to `i` squared.


list_test = []
for x in range(1, 11):
    y = x ** 2
    list_test.append((x, y))
print(list_test)

# Второй вариант

list_test2 = [(x, x*x) for x in range(1, 11)]

print(list_test2)
