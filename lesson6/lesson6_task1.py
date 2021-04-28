# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.


while True:
    sentence = input("Type any sentence you like using only spaces without any symbols. "
                     "Please use only one space between words and at the end of the sentence.\n")
    sentence_list = sentence.split(" ")
    if sentence_list.count("") <= 0:
        break
    print("You have added more that one space between words or at the and of the sentence. Try again.\n")

dic = {key: sentence_list.count(key) for key in sentence_list}
print(dic)
