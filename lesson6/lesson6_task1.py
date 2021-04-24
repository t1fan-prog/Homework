# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.


sentence = input("Type any sentence you like using only spaces without any symbols:\n")

sentence_list = sentence.split(" ")

dic = {}
for i in sentence_list:
    dic[i] = sentence_list.count(i)

print(dic)
