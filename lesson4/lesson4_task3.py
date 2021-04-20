import random

word = input("Enter any word you like:\n")

for _ in range(5):
    word_list = list(word)
    random.shuffle(word_list)
    result = ''.join(word_list)
    print(result)
